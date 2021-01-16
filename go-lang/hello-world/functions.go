package main

import (
	"fmt"
	"math"
)

func percentile(x []float64, k float64) (float64, uint32) { // like Python - Go allows returning multiple values.
	rank := ((k * 0.01) * float64(len(x)-1)) + 1.0
	rankLow := math.Floor(rank)
	rankHigh := math.Ceil(rank)
	var result float64 = 0

	if rankHigh != rankLow {
		result = x[int(rankLow)-1] + ((x[int(rankHigh)-1] - x[int(rankLow)-1]) * (rank - rankLow))
	} else {
		result = x[int(rankLow)-1]
	}
	return result, 23
}

func namedReturn() (r int) { // creates variables that are automatically returned.
	r = 5
	return r
}

func variadicSum(k int, x ...int) int {
	total := 0
	for _, n := range x {
		total += n
	}
	total += k
	return total
}

/*
Deferred function example
*/
func first() {
	fmt.Println("1st")
}

func second() {
	fmt.Println("2nd")
}

func deferTest() {
	// deferred function is run before return or in an event of a Panic
	defer second() // schedules second() to be called at the end; Equivalent to finally.
	first()
}

/*Panic recover example*/
func panicTest() {
	panic("PANIC")
}




func main() {

	// The line below does not work due to
	// https://stackoverflow.com/questions/29518109/why-does-defer-recover-not-catch-panics
	//defer recover()

	defer func() { // recover has to be called after panic() executes
		p := recover()
		fmt.Println(p, "recovered")
	}()

	fmt.Println("functions")
	v := []float64 {1,2,3,4,5,6,7,8,9,10}
	x := []int {1,2,3,4,5}
	fmt.Println(percentile(v, 50))
	fmt.Println(namedReturn())
	// Variadic args can be given manually or using the 'unpack' operation indicated by the ... suffix.
	fmt.Println(variadicSum(-100, 1, 2, 3, 4))
	fmt.Println(variadicSum(-100, x...))

	z := int32(20)
	add := func (x int32 , y int32) int32 { // Go also supports anonymous functions.
		return x + y + z // z accessed from outer scope.
	}
	fmt.Println(add(2,3))

	deferTest()
	panicTest()

}