package main

import "fmt"

func toLowerCase(s string) string {
	var newString []byte
	for i := 0; i < len(s); i++ {
		if s[i] >= 'A' && s[i] <= 'Z' {
			newString = append(newString, s[i]-'A'+'a')
		} else {
			newString = append(newString, s[i])
		}
	}
	return string(newString)
}

func main() {
	s := "LOVELY"
	fmt.Println(toLowerCase(s))
}
