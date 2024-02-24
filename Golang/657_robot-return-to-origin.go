package main

import "fmt"

func judgeCircle(moves string) bool {
	timesArray := [4]int{0}
	direMap := map[uint8]int{'R': 0, 'L': 1, 'U': 2, 'D': 3}
	// R:0, L:1, U:2, D:3
	for idx := 0; idx < len(moves); idx++ {
		timesArray[direMap[moves[idx]]]++
	}
	if timesArray[0] == timesArray[1] && timesArray[2] == timesArray[3] {
		return true
	}
	return false
}

func main() {
	moves := "UD"
	fmt.Println(judgeCircle(moves))
}
