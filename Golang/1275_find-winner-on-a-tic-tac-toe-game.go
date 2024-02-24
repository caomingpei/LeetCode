package main

import "fmt"

func check(board [3][3]int) string {
	winner := map[int]string{0: "A", 1: "B"}
	for i := 0; i < 3; i++ {
		if board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][0] != -1 {
			return winner[board[i][0]]
		}
		if board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[0][i] != -1 {
			return winner[board[0][i]]
		}
	}
	if board[0][0] == board[1][1] && board[0][0] == board[2][2] && board[1][1] != -1 {
		return winner[board[1][1]]
	}
	if board[2][0] == board[1][1] && board[1][1] == board[0][2] && board[1][1] != -1 {
		return winner[board[1][1]]
	}
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			if board[i][j] == -1 {
				return "Pending"
			}
		}
	}
	return "Draw"
}

func tictactoe(moves [][]int) string {
	board := [3][3]int{
		{-1, -1, -1},
		{-1, -1, -1},
		{-1, -1, -1},
	}
	for idx := 0; idx < len(moves); idx++ {
		val := moves[idx]
		board[val[0]][val[1]] = idx % 2
	}
	return check(board)
}

func main() {
	moves := [][]int{{0, 0}, {1, 1}}
	fmt.Println(tictactoe(moves))
}
