package message

import (
	"reflect"
	"testing"
	"time"

	"github.com/n0stack/n0core/model"
	uuid "github.com/satori/go.uuid"
	yaml "gopkg.in/yaml.v2"
)

func TestNotificationUnmarshalYAML(t *testing.T) {
	c, _ := model.NewCompute("1578ce2b-b845-41b2-9c73-7e05009785e6", "testing", "test_model", map[string]string{"hoge": "hoge"}, model.Dependencies{}, []string{"test/test"})

	taskID, _ := uuid.FromString("2efbfd8d-6136-4390-a513-033e7c5f2391")
	mes := &Notification{
		TaskID:      taskID,
		Task:        "Hoge",
		NotifiedAt:  time.Date(2000, 1, 1, 0, 0, 0, 0, time.UTC),
		Operation:   "Hoge",
		IsSucceeded: true,
		Description: "foobar",
		Model:       c,
	}

	y, err := yaml.Marshal(mes)
	if err != nil {
		t.Errorf("Failed to marshal message to yaml: error message %v", err.Error())
	}
	t.Logf("%v", string(y))

	r := []byte(`taskID: 2efbfd8d-6136-4390-a513-033e7c5f2391
task: Hoge
notifiedAt: 2000-01-01T00:00:00Z
operation: Hoge
isSucceeded: true
description: foobar
model:
  id: 1578ce2b-b845-41b2-9c73-7e05009785e6
  type: node/compute
  state: testing
  name: test_model
  meta:
    hoge: hoge
  dependencies: []
  supportingTypes:
  - test/test
`)
	if !reflect.DeepEqual(r, y) {
		t.Errorf("Failed to marshal to yaml:\ngot\n%v\nwant\n%v", string(y), string(r))
	}

	n := Notification{}
	err = yaml.Unmarshal(y, &n)
	if err != nil {
		t.Errorf("Failed to unmarshal message to yaml: error message %v", err.Error())
	}
	if !reflect.DeepEqual(*mes, n) {
		t.Errorf("Failed to unmarshal to yaml:\ngot  %v,\nwant %v", n, *mes)
	}
}
