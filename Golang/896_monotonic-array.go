package main

import "fmt"

func isMonotonic(nums []int) bool {
	flagI, flagJ := true, true
	maxLen := len(nums)
	i, j := 1, maxLen-2
	for i < maxLen && j >= 0 {
		if nums[i] < nums[i-1] {
			flagI = false
		}
		if nums[j] < nums[j+1] {
			flagJ = false
		}
		i++
		j--
	}
	return flagI || flagJ
}

func main() {
	nums := []int{1, 3, 2}
	fmt.Println(isMonotonic(nums))
}
