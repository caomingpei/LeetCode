package main

import "fmt"

func findTheDifference(s string, t string) byte {
	bMap := make(map[byte]int)
	for i := 0; i < len(t); i++ {
		bMap[t[i]] += 1
	}
	for j := 0; j < len(s); j++ {
		bMap[s[j]] -= 1
	}
	for k, val := range bMap {
		if val != 0 {
			return k
		}
	}
	return 0
}

func main() {
	s, t := "abcd", "abcde"
	fmt.Printf("%c", findTheDifference(s, t))
}
