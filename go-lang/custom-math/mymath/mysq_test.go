package mymath

import (
	"fmt"
	"testing"
)

func TestSq(t *testing.T) {
	fmt.Println("In test")
	x := Sq(2.0)
	expect := 6.0
	if x != expect {
		t.Errorf("expected = %f actual = %f", expect, x)
	}
}
