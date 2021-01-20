package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	fmt.Println("here we are.....")
	file, err := os.Open("input.json")
	if err != nil {
		fmt.Println("failed to open failed")
		return
	}

	// stat, err := file.Stat()
	// if err != nil {
	// 	fmt.Println("Failed stat check")
	// 	return
	// }

	bytes := make([]byte, 50)
	for {
		n, err := file.Read(bytes)
		if err != nil {
			fmt.Println(err)
			break
		}

		if n <= 0 {
			break
		}

		content := string(bytes[0:n])
		fmt.Println(content)
		fmt.Println("____")
	}

	file.Close()

	fmt.Println("___________ Reading with io-util")
	bytes, err = ioutil.ReadFile("input.json")
	content := string(bytes)
	if err != nil {
		fmt.Println("failed with io utils")
	}
	fmt.Println(content)
}
