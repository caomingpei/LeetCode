package main

import "fmt"

func plusOne(digits []int) []int {
	maxLen := len(digits)
	flag := 0
	for i := maxLen - 1; i >= 0; i-- {
		if digits[i] != 9 {
			digits[i]++
			return digits
		} else {
			flag = 1
			digits[i] = 0
		}
	}
	if flag == 1 {
		return append([]int{1}, digits...)
	}
	return digits
}

func main() {
	digits := []int{9, 9}
	fmt.Println(plusOne(digits))
}
