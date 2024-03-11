package main

import (
	"fmt"
	"strings"
)

func capitalizeTitle(title string) string {
	words := strings.Split(title, " ")
	var ans []string
	for _, word := range words {
		if len(word) > 2 {
			ans = append(ans, strings.ToUpper(string(word[0]))+strings.ToLower(word[1:]))
		} else {
			ans = append(ans, strings.ToLower(word))
		}
	}
	return strings.Join(ans, " ")
}

func main() {
	title := "capiTalIze tHe titLe"
	fmt.Println(capitalizeTitle(title))
}
