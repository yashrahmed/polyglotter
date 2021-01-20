package main

import (
	"container/list"
	"fmt"
	"sort"
)

type Person struct {
	name string
	age  int
}

type People []Person // renaming types

// Implementing the 3 methods of the sort interface
// methods can be attached to custom types.
func (x People) Len() int {
	return len(x)
}

func (x People) Less(i, j int) bool {
	return x[i].age <= x[j].age // enable sorting by age
}

func (x People) Swap(i, j int) {
	x[i], x[j] = x[j], x[i]
}

func main() {

	fmt.Println("Lists and sorting")

	// a list pointer can be created using list.New()
	var x list.List // default value is an empty list and not nil
	x.PushBack(1)
	x.PushBack(3)
	x.PushBack(2)

	for e := x.Front(); e != nil; e = e.Next() {
		fmt.Println(e.Value)
	}

	var people People = []Person{
		Person{"yash", 31},
		Person{"Maulik", 30},
	}

	sort.Sort(people)
	fmt.Println(people)

}
