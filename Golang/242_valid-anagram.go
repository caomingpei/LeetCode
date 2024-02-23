package main

import "fmt"

func isAnagram(s string, t string) bool {
	buckTemp := [26]int{0}
	for i := range s {
		buckTemp[s[i]-'a']++
	}
	for j := range t {
		buckTemp[t[j]-'a']--
	}
	for k := 0; k < len(buckTemp); k++ {
		if buckTemp[k] != 0 {
			return false
		}
	}
	return true
}

func main() {
	s, t := "anagram", "nagaram"
	fmt.Println(isAnagram(s, t))
}
