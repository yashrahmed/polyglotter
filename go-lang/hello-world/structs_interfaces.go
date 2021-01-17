package main

import "fmt"

type Square struct {
	x, y, l int
}

func (s *Square) area() int { // function area is a "method" of struct Sqaure
	return s.l * s.l
}

type Rect struct {
	x, y, l, b int
}

func (r *Rect) area() int { // This function is a method of the struct Rect
	return r.l * r.b
}

// Note that nowhere in the program is specified that Rect and Square implement Areas
// This is inferred by the compiler..
type Areas interface { // define interface
	area() int
}

func rectAreaCopy(r Rect) int { // Entire instance is copied by value
	return r.l * r.b
}

func rectArea(r *Rect) int {
	return r.l * r.b
}

func main() {

	// 3 different types of initialization
	var rect Rect = Rect{x: 1, y: 2, l: 5, b: 5} // field names can be ignored.
	rect2 := Rect{x: 2, y: 2, l: 5, b: 5}
	var rect3 *Rect = new(Rect)
	*rect3 = Rect{x: 3, y: 3, l: 5, b: 5}

	fmt.Println("x =", rect.x, " y =", rect.y)
	fmt.Println("x =", rect2.x, " y =", rect2.y)
	fmt.Println("x =", rect3.x, " y =", rect3.y) // note that struct fields can be accessed without dereferencing.

	fmt.Println(rectArea(rect3))
	fmt.Println(rect.area())

	//https://stackoverflow.com/questions/40823315/x-does-not-implement-y-method-has-a-pointer-receiver
	sq := Square{0, 0, 2}
	var a Areas = &rect // interface can "refer" to a concrete type but var a Areas = rect is invalid.
	var a2 Areas = &sq
	fmt.Println(a.area())
	fmt.Println(a2.area())
}
