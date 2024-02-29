package main

import "fmt"

func setZeroes(matrix [][]int) {
	m, n := len(matrix), len(matrix[0])
	rows, cols := make([]int, m), make([]int, n)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == 0 {
				rows[i], cols[j] = 1, 1
			}
		}
	}
	for i := 0; i < m; i++ {
		if rows[i] == 1 {
			for j := 0; j < n; j++ {
				matrix[i][j] = 0
			}
		}
	}
	for j := 0; j < n; j++ {
		if cols[j] == 1 {
			for i := 0; i < m; i++ {
				matrix[i][j] = 0
			}
		}
	}
	fmt.Println(matrix)
}

func main() {
	matrix := [][]int{{0, 1, 2, 0}, {3, 4, 5, 2}, {1, 3, 1, 5}}
	setZeroes(matrix)
}
