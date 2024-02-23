package main

import (
	"fmt"
)

func arraySign(nums []int) int {
	flag := 1
	for i := 0; i < len(nums); i++ {
		if nums[i] < 0 {
			flag *= -1
		} else if nums[i] == 0 {
			return 0
		}
	}
	return flag
}

func main() {
	nums := []int{-1, -2, -3, -4, 3, 2, 1}
	fmt.Println(arraySign(nums))
}
