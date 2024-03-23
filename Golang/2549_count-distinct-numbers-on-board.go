package main

import "fmt"

func distinctIntegers(n int) int {
	if n > 1 {
		return n - 1
	} else {
		return 1
	}
}

func main() {
	n := 5
	fmt.Println(distinctIntegers(n))
}
