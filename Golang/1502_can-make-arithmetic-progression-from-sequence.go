package main

import (
	"fmt"
	"sort"
)

func canMakeArithmeticProgression(arr []int) bool {
	sort.Ints(arr)
	candi := arr[1] - arr[0]
	for i := 1; i < len(arr); i++ {
		if arr[i]-arr[i-1] != candi {
			return false
		}
	}
	return true
}

func main() {
	arr := []int{3, 4, 1}
	fmt.Println(canMakeArithmeticProgression(arr))
}
