package main

import (
	"fmt"
)

/*

Go map is an un-ordered collection.

*/

func main() {
	fmt.Println("here.....")
	// map type is read as map[key-type]value
	// nested type is read as map[lvl1-key-type]map[lvl2-key-type]...value-type
	var x map[string]int = make(map[string]int) // make is used to initialize maps and arrays.
	x["key"] = 10
	fmt.Println(x)
	//delete(x, "key") // delete "key" entry.
	//fmt.Println(x)
	fmt.Println(x["key2"]) // Missing key does not throw an exception but returns default value.
	val, ok := x["key2"] // Better way to check if variable exists.
	fmt.Println(val, ok)
	// This can be used in an if statement
	if val, ok := x["key"]; ok {
		fmt.Println("value = ", val)
	}

	/*
	Array init shorthand
	*/
	var countryToCapitalToPop map[string]map[string]int32 = map[string]map[string]int32 {
		"Washington DC" : map[string]int32 {
			"USA": 300,
		},
		"Beijing" : map[string]int32 {
			"China": 1400,
		},
	}
	fmt.Println(countryToCapitalToPop)
}