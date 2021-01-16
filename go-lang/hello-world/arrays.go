package main

import (
	"fmt"
	"math"
)

func main() {
	// array of type T is written as [n]Type;. Leave n blank for array of unknown size.
	var (
		 x [10] float64
		 input float64
		 percentile float64
	)

	for i := 0 ; i < 10; i++ {
		x[i] = (float64)(i + 1) // type conversion syntax is type(expr)
	}
	y := [5]int32 {9,8,7,6,5} // alternate syntax for array declaration.
	for _, p := range y { // Python like _ syntax allowed.
		fmt.Println(p)
	}
	var y2 []int32 = y[2:4] // python like slicing allowed.
	var yApp []int32 = append(y2, -1, -2, -3) // append to array and create a new one.
	// copy() for creating a copy of an array.
	fmt.Println(y2)
	y2[1] = 100
	fmt.Println(yApp) // unlike python array slices can modify the original array.
	fmt.Println(y)


	fmt.Println(x)
	fmt.Scanf("%f", &input)

	//compute median
	rank := ((input / 100.0) * 9) + 1.0
	rankLow := int(math.Floor(rank))
	rankHigh := int(math.Ceil(rank))

	if rankLow < rankHigh {
		percentile = float64(rankLow) + (x[rankHigh - 1] - x[rankLow - 1]) * (rank - float64(rankLow))
	} else {
		percentile = x[int(rank)-1]
	}
	fmt.Println(percentile)
}