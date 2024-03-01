package main

import "fmt"

func checkStraightLine(coordinates [][]int) bool {
	if len(coordinates) == 2 {
		return true
	}
	point1, point2 := coordinates[0], coordinates[1]
	x1, x2, y1, y2 := point1[0], point2[0], point1[1], point2[1]

	for i := 2; i < len(coordinates); i++ {
		x, y := coordinates[i][0], coordinates[i][1]
		if x1 == x2 {
			if x != x1 {
				return false
			}
			continue
		}
		if y1 == y2 {
			if y != y1 {
				return false
			}
			continue
		}
		left := float64(y-y2) / float64(y1-y2)
		right := float64(x-x2) / float64(x1-x2)
		if abs1232(left-right) > 1e-6 {
			return false
		}
	}
	return true
}
func abs1232(a float64) float64 {
	if a < 0 {
		return -a
	}
	return a
}

func main() {
	coordinates := [][]int{{0, 1}, {2, 4}, {3, 3}}
	fmt.Println(checkStraightLine(coordinates))
}
