package main

import (
	"flag"
	"fmt"
)

func main() {
	fpath := flag.String("path", "", "path to file")
	flag.Parse()
	if *fpath == "" {
		fmt.Println("-path must be specified")
	} else {
		fmt.Println("fpath  =", *fpath)
	}
}
