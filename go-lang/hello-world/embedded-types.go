package main

import "fmt"

type Rect struct {
	l, b int
}

func (r *Rect) area() int {
	return r.l * r.b
}

type Square struct {
	Rect // Rect is embedde here. represents an is-a relationship.
	s    int
}

func main() {
	fmt.Println("here....")
	sq := Square{Rect: Rect{l: 2, b: 2}, s: 2} // embedded types are intialized thus..better to write "constructors"
	fmt.Println(sq.area())
}
