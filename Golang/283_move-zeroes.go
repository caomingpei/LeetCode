package main

import "fmt"

func moveZeroes(nums []int) {
	b := 0
	for a := 0; a < len(nums); a++ {
		if nums[a] != 0 {
			tmp := nums[a]
			nums[a] = nums[b]
			nums[b] = tmp
			b++
		}
	}
	fmt.Println(nums)
}

func main() {
	nums := []int{0, 1, 0, 3, 12}
	moveZeroes(nums)
}
