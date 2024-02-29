package main

import "fmt"

func maximumWealth(accounts [][]int) int {
	m := len(accounts)
	n := len(accounts[0])
	maxNum := 0
	for i := 0; i < m; i++ {
		cur := 0
		for j := 0; j < n; j++ {
			cur += accounts[i][j]
		}
		maxNum = max(maxNum, cur)
	}
	return maxNum
}

func main() {
	accounts := [][]int{{1, 2, 3}, {3, 2, 1}}
	fmt.Println(maximumWealth(accounts))
}
