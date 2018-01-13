package model

import (
	"path/filepath"
	"reflect"
	"testing"

	"github.com/satori/go.uuid"
)

func TestNetworkToModel(t *testing.T) {
	id := uuid.NewV4()
	m := &Model{
		ID:           id,
		Type:         "test/test",
		State:        "testing",
		Name:         "test_model",
		Meta:         map[string]string{"hoge": "hoge"},
		Dependencies: Dependencies{},
	}

	n := &Network{
		Model:   *m,
		Bridge:  "nbr-test",
		Subnets: []Subnet{},
	}

	f := n.ToModel()

	if !reflect.DeepEqual(f, m) {
		t.Errorf("Got another model on ToModel:\ngot  %v\nwant %v", f, m)
	}
}

func TestNewNetwork(t *testing.T) {
	id := uuid.NewV4()
	specificType := "hoge"
	m := &Model{
		ID:           id,
		Type:         filepath.Join(NetworkType, specificType),
		State:        "testing",
		Name:         "test_model",
		Meta:         map[string]string{"hoge": "hoge"},
		Dependencies: Dependencies{},
	}

	v := &Network{
		Model:   *m,
		Bridge:  "nbr-test",
		Subnets: []Subnet{},
	}

	nv := NewNetwork(v.ID, specificType, v.State, v.Name, v.Meta, v.Dependencies, v.Bridge, v.Subnets)

	if !reflect.DeepEqual(v, nv) {
		t.Errorf("Got another model on NewVM:\ngot  %v\nwant %v", v, nv)
	}
}