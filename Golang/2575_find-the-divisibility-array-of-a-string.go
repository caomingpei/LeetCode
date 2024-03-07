package main

import "fmt"

func divisibilityArray(word string, m int) []int {
	var ans []int
	cur := 0
	for i := 0; i < len(word); i++ {
		cur = (cur*10 + int(word[i]-'0')) % m
		if cur == 0 {
			ans = append(ans, 1)
		} else {
			ans = append(ans, 0)
		}
	}
	return ans
}

func main() {
	word := "998244353"
	m := 3
	fmt.Println(divisibilityArray(word, m))
}
