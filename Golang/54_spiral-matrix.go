package main

import "fmt"

func spiralOrder(matrix [][]int) []int {
	m, n := len(matrix), len(matrix[0])
	visited := make([][]bool, m)
	all := m * n
	ans := make([]int, all)
	for i := 0; i < m; i++ {
		visited[i] = make([]bool, n)
	}
	dir := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	round := 0
	nowM, nowN := 0, 0
	for i := 0; i < all; i++ {
		ans[i] = matrix[nowM][nowN]
		visited[nowM][nowN] = true
		nextM, nextN := nowM+dir[round][0], nowN+dir[round][1]
		if nextM < 0 || nextM >= m || nextN < 0 || nextN >= n || visited[nextM][nextN] {
			round = (round + 1) % 4
		}
		nowM, nowN = nowM+dir[round][0], nowN+dir[round][1]
	}
	return ans
}

func main() {
	matrix := [][]int{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}}
	fmt.Println(spiralOrder(matrix))
}
