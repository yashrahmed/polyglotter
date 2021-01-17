package main

import "fmt"

func doublePtr(x *int) { // x if of type int pointer.
	fmt.Println(x, " in func")
	*x *= 2 // *x dereferences a pointer. i.e. value at address held in x
}

func swap(x *int, y *int) {
	t := *x
	*x = *y
	*y = t
}

func main() {

	a := 1
	b := 2
	fmt.Println(a, b)
	swap(&a, &b)
	fmt.Println(a, b)

	var p *int = new(int) // new function returns a pointer after allocating memory.
	*p = 10
	fmt.Println(p)
	fmt.Println(*p)

	k := 2
	fmt.Println(&k)
	doublePtr(&k) // & returns a pointer to a variable.
	fmt.Println(k)
}