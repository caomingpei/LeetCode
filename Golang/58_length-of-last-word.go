package main

import "fmt"

func lengthOfLastWord(s string) int {
	startInd := len(s) - 1

	for startInd >= 0 {
		if s[startInd] != ' ' {
			break
		}
		startInd--
	}

	for i := startInd; i >= 0; i-- {
		if s[i] == ' ' {
			return startInd - i
		}
	}
	return startInd + 1
}

func main() {
	s := "luffy is still joyboy"
	fmt.Println(lengthOfLastWord(s))
}
