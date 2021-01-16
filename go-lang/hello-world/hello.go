package main

import "fmt"
import "rsc.io/quote"

//one line comment
/*
Multiline comment.
*/

func main() {
	// Go has Java like closure rules. No hoisting.
	//'' are for character literals.
	var input uint32
	var x string // short hand is x := "Hello"
	x = "Hello" // type is optional if written in the same line. Go compiler can auto-infer type.
	const ( // this syntax is useful for declaring multiple variables.
		y string = " World"
	)
	fmt.Println(x + y)
	fmt.Println(quote.Go())
	fmt.Scanf("%d", &input)
	fmt.Println("The number you entered is ", input)

	var i uint32 = 0
	for i < input { // if initializer is present i:=0; i < input; i++ {} statement can be used
		if i % 2 == 0 {
			fmt.Println(i)
		}
		switch i {
			case 5: fmt.Println("@5")
			default: 
		}
		i++
	}
}
