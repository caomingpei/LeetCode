package main

import "fmt"

func findKOr(nums []int, k int) int {
	maxLen := 31
	ans := 0
	for i := 0; i < maxLen; i++ {
		cnt := 0
		for _, num := range nums {
			if (num>>i)&1 == 1 {
				cnt++
			}
		}
		if cnt >= k {
			ans |= 1 << i
		}
	}
	return ans
}

func main() {
	nums := []int{2, 12, 1, 11, 4, 5}
	k := 6
	fmt.Println(findKOr(nums, k))
}
