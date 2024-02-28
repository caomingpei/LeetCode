package main

import (
	"fmt"
)

type TreeNoe2673 struct {
	Val   int
	Left  *TreeNoe2673
	Right *TreeNoe2673
}

func minIncrements(n int, cost []int) int {
	ans := 0
	for i := n - 2; i > 0; i -= 2 {
		ans += abs(cost[i] - cost[i+1])
		cost[i/2] = cost[i/2] + max(cost[i], cost[i+1])
	}
	return ans
}
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	n := 7
	cost := []int{1, 5, 2, 2, 3, 3, 1}
	fmt.Println(minIncrements(n, cost))
}
