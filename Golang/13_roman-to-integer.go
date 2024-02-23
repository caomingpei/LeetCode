package main

import "fmt"

func romanToInt(s string) (ans int) {
	romanMap := map[byte]int{'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	n := len(s)
	for i := range s {
		value := romanMap[s[i]]
		if i < n-1 && value < romanMap[s[i+1]] {
			ans -= value
		} else {
			ans += value
		}
	}
	return
}

func main() {
	s := "MCMXCIV"
	fmt.Println(romanToInt(s))
}
