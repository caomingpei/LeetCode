package main

import "fmt"

func check1041(runUnit [4]int) bool {
	if runUnit[0] == runUnit[2] && runUnit[1] == runUnit[3] {
		return false
	}
	return true
}

func isRobotBounded(instructions string) bool {
	dir := 0
	var runUnit [4]int
	for idx := 0; idx < len(instructions); idx++ {
		ins := instructions[idx]
		if ins == 'G' {
			runUnit[dir]++
		} else if ins == 'L' {
			dir = (dir + 1) % 4
		} else if ins == 'R' {
			dir = (dir + 3) % 4
		}
	}
	if dir == 0 && check1041(runUnit) {
		return false
	}
	return true
}

func main() {
	instructions := "GGLLGG"
	fmt.Println(isRobotBounded(instructions))
}
