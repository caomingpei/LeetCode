package main

import "fmt"

func mergeAlternately(word1 string, word2 string) string {
	m, n := len(word1), len(word2)
	byteTemp := make([]byte, 0, m+n)
	for i := 0; i < m || i < n; i++ {
		if i < m {
			byteTemp = append(byteTemp, word1[i])
		}
		if i < n {
			byteTemp = append(byteTemp, word2[i])
		}

	}
	return string(byteTemp)
}

func main() {
	word1 := "ab"
	word2 := "pqrs"
	fmt.Println(mergeAlternately(word1, word2))
}
