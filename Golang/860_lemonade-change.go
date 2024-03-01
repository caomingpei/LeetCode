package main

import "fmt"

func lemonadeChange(bills []int) bool {
	cashier := [2]int{}
	for i := 0; i < len(bills); i++ {
		if bills[i] == 5 {
			cashier[0]++
		} else if bills[i] == 10 {
			if cashier[0] > 0 {
				cashier[0]--
				cashier[1]++
			} else {
				return false
			}
		} else if bills[i] == 20 {
			if cashier[1] > 0 && cashier[0] > 0 {
				cashier[1]--
				cashier[0]--
			} else if cashier[0] >= 3 {
				cashier[0] -= 3
			} else {
				return false
			}
		}
	}
	return true
}

func main() {
	bills := []int{5, 5, 5, 10, 20}
	fmt.Println(lemonadeChange(bills))
}
