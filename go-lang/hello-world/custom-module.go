package main

import (
	"custom-math/mymath"
	"custom-math/mymath/squaring" // nested nodule import
	"fmt"
)

func main() {
	fmt.Println(mymath.Sq(4))
	fmt.Println(squaring.Sq(4))
}
