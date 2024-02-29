package main

import "fmt"

func diagonalSum(mat [][]int) int {
	n := len(mat)
	ans := 0
	for i := 0; i < n; i++ {
		ans += mat[i][i]
		mat[i][i] = -1
	}
	for i := 0; i < n; i++ {
		if mat[i][n-1-i] == -1 {
			continue
		}
		ans += mat[i][n-1-i]
	}
	return ans
}

func main() {
	mat := [][]int{
		{1, 1, 1, 1},
		{1, 1, 1, 1},
		{1, 1, 1, 1},
		{1, 1, 1, 1},
	}
	fmt.Println(diagonalSum(mat))
}
