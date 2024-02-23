package main

import "fmt"

func strStr(haystack string, needle string) int {
	n, m := len(haystack), len(needle)
outer:
	for i := 0; i+m <= n; i++ {
		for j := range needle {
			if haystack[i+j] != needle[j] {
				continue outer
			}
		}
		return i
	}
	return -1
}

func main() {
	haystack, needle := "sadbutsad", "sad"
	fmt.Println(strStr(haystack, needle))
}
