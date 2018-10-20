package dag

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"reflect"
	"sync"

	"github.com/n0stack/n0stack/n0proto/deployment/v0"
	"github.com/n0stack/n0stack/n0proto/pool/v0"
	"github.com/n0stack/n0stack/n0proto/provisioning/v0"

	"google.golang.org/grpc"
)

type Task struct {
	ResourceType string                 `yaml:"resource_type"`
	Action       string                 `yaml:"action"`
	Args         map[string]interface{} `yaml:"args"`
	DependOn     []string               `yaml:"depend_on"`
	// Rollback []*Task `yaml:"rollback"`

	child   []string
	depends int
}

// return response JSON bytes
func (a Task) Do(conn *grpc.ClientConn) ([]byte, error) {
	var grpcCliType reflect.Type
	var grpcCliValue reflect.Value

	// TODO :生成自動化
	switch a.ResourceType {
	case "node", "Node":
		grpcCliType = reflect.TypeOf(ppool.NewNodeServiceClient(conn))
		grpcCliValue = reflect.ValueOf(ppool.NewNodeServiceClient(conn))
	case "network", "Network":
		grpcCliType = reflect.TypeOf(ppool.NewNetworkServiceClient(conn))
		grpcCliValue = reflect.ValueOf(ppool.NewNetworkServiceClient(conn))
	case "block_storage", "BlockStorage":
		grpcCliType = reflect.TypeOf(pprovisioning.NewBlockStorageServiceClient(conn))
		grpcCliValue = reflect.ValueOf(pprovisioning.NewBlockStorageServiceClient(conn))
	case "virtual_machine", "VirtualMachine":
		grpcCliType = reflect.TypeOf(pprovisioning.NewBlockStorageServiceClient(conn))
		grpcCliValue = reflect.ValueOf(pprovisioning.NewBlockStorageServiceClient(conn))
	case "image", "Image":
		grpcCliType = reflect.TypeOf(pdeployment.NewImageServiceClient(conn))
		grpcCliValue = reflect.ValueOf(pdeployment.NewImageServiceClient(conn))
	case "flavor", "Flavor":
		grpcCliType = reflect.TypeOf(pdeployment.NewFlavorServiceClient(conn))
		grpcCliValue = reflect.ValueOf(pdeployment.NewFlavorServiceClient(conn))
	default:
		return nil, fmt.Errorf("Resource type '%s' do not exist", a.ResourceType)
	}

	fnt, ok := grpcCliType.MethodByName(a.Action)
	if !ok {
		return nil, fmt.Errorf("Resource type '%s' do not have action '%s'", a.ResourceType, a.Action)
	}

	// 1st arg is instance, 2nd is context.Background()
	// TODO: 何かがおかしい、 argsElem is "**SomeMessage", so use argsElem.Elem() in Call
	argsType := fnt.Type.In(2)
	argsElem := reflect.New(argsType)
	if a.Args == nil {
		a.Args = make(map[string]interface{})
	}
	buf, err := json.Marshal(a.Args)
	if err != nil {
		return nil, fmt.Errorf("Args is invalid, set fields of message '%s' err=%s", argsType.String(), err.Error())
	}
	if err := json.Unmarshal(buf, argsElem.Interface()); err != nil {
		return nil, fmt.Errorf("Args is invalid, set fields of message '%s' err=%s", argsType.String(), err.Error())
	}

	out := fnt.Func.Call([]reflect.Value{grpcCliValue, reflect.ValueOf(context.Background()), argsElem.Elem()})
	if err, _ := out[1].Interface().(error); err != nil {
		return nil, fmt.Errorf("got error response: %s", err.Error())
	}

	res, _ := json.Marshal(out[0].Interface())

	return res, nil
}

// topological sort
// 実際遅いけどもういいや O(E^2 + V)
func IsDAG(tasks map[string]*Task) bool {
	result := 0

	for k, _ := range tasks {
		tasks[k].child = make([]string, 0)
		tasks[k].depends = len(tasks[k].DependOn)
	}

	for k, v := range tasks {
		for _, d := range v.DependOn {
			tasks[d].child = append(tasks[d].child, k)
		}
	}

	s := make([]string, 0, len(tasks))
	for k, v := range tasks {
		if v.depends == 0 {
			s = append(s, k)
			result++
		}
	}

	for len(s) != 0 {
		n := s[len(s)-1]
		s = s[:len(s)-1]

		for _, c := range tasks[n].child {
			tasks[c].depends--
			if tasks[c].depends == 0 {
				s = append(s, c)
				result++
			}
		}
	}

	return result == len(tasks)
}

type ActionResult struct {
	Name string
	Json []byte
	Err  error
}

// 出力で時間を出したほうがよさそう
func DoDAG(tasks map[string]*Task, out io.Writer, conn *grpc.ClientConn) bool {
	for k, _ := range tasks {
		tasks[k].child = make([]string, 0)
		tasks[k].depends = len(tasks[k].DependOn)
	}

	for k, v := range tasks {
		for _, d := range v.DependOn {
			tasks[d].child = append(tasks[d].child, k)
		}
	}

	resultChan := make(chan ActionResult, 100)
	wg := new(sync.WaitGroup)
	total := len(tasks)
	done := 0

	doTask := func(taskName string) {
		defer wg.Done()

		result, err := tasks[taskName].Do(conn)
		resultChan <- ActionResult{
			Name: taskName,
			Json: result,
			Err:  err,
		}
	}

	for k, v := range tasks {
		if v.depends == 0 {
			wg.Add(1)
			fmt.Fprintf(out, "---> Task '%s' is started\n", k)
			log.Printf("[DEBUG] Task '%s' is started: %+v", k, v)
			go doTask(k)
		}
	}

	failed := false
	for r := range resultChan {
		done++

		if r.Err != nil {
			fmt.Fprintf(out, "---> [ %d/%d ] Task '%s' is failed: %s\n", done, total, r.Name, r.Err.Error())

			if !failed {
				failed = true

				// すでにリクエストしたタスクの終了を待つ
				fmt.Fprintf(out, "---> Wait to finish requested tasks\n")
				go func() {
					wg.Wait()
					close(resultChan)
				}()
			}
		} else {
			buf := &bytes.Buffer{}
			json.Indent(buf, r.Json, "", "  ")
			if failed {
				fmt.Fprintf(out, "---> [ %d/%d ] Task '%s', which was requested until failed, is finished\n--- Response ---\n%s\n", done, total, r.Name, buf.String())
			} else {
				fmt.Fprintf(out, "---> [ %d/%d ] Task '%s' is finished\n--- Response ---\n%s\n", done, total, r.Name, buf.String())

				// queueing
				for _, d := range tasks[r.Name].child {
					tasks[d].depends--
					if tasks[d].depends == 0 {
						wg.Add(1)
						fmt.Fprintf(out, "---> Task '%s' is started\n", d)
						log.Printf("[DEBUG] Task '%s' is started: %+v", d, tasks[d])
						go doTask(d)
					}
				}
			}
		}

		if !failed && done == total {
			close(resultChan)
		}
	}

	if failed {
		// TODO: rollback

		return false
	}

	return true
}
