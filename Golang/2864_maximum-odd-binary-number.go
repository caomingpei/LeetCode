package main

import (
	"fmt"
	"strings"
)

func maximumOddBinaryNumber(s string) string {
	var nums [2]int
	for i := 0; i < len(s); i++ {
		nums[s[i]-'0']++
	}
	if nums[1] == 1 {
		return strings.Repeat("0", nums[0]) + strings.Repeat("1", 1)
	} else {
		return strings.Repeat("1", nums[1]-1) + strings.Repeat("0", nums[0]) + strings.Repeat("1", 1)
	}
}

func main() {
	s := "0101"
	fmt.Println(maximumOddBinaryNumber(s))
}
