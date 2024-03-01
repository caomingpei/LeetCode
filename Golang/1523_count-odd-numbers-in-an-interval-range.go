package main

import "fmt"

func countOdds(low int, high int) int {
	if low%2 == 0 && high%2 == 0 {
		return (high - low) / 2
	}
	return (high-low)/2 + 1
}

func main() {
	low, high := 3, 7
	fmt.Println(countOdds(low, high))
}
