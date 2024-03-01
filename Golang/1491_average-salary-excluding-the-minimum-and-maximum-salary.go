package main

import "fmt"

func average(salary []int) float64 {
	maxS, minS := 0, int(1e6)
	sum := 0
	for i := 0; i < len(salary); i++ {
		maxS = max1491(maxS, salary[i])
		minS = -max1491(-minS, -salary[i])
		sum += salary[i]
	}
	return float64(sum-maxS-minS) / float64(len(salary)-2)
}

func max1491(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	salary := []int{4000, 3000, 1000, 2000}
	fmt.Println(average(salary))
}
