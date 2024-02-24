package main

import (
	"container/list"
	"fmt"
	"strconv"
)

func calPoints(operations []string) int {
	stack := list.New()
	for idx := range operations {
		value := operations[idx]
		intVal, err := strconv.Atoi(value)
		if err == nil {
			stack.PushBack(intVal)
		} else if value == "+" {
			last := stack.Back().Value.(int)
			lastPrev := stack.Back().Prev().Value.(int)
			stack.PushBack(last + lastPrev)
		} else if value == "D" {
			last := stack.Back().Value.(int)
			stack.PushBack(last * 2)
		} else if value == "C" {
			stack.Remove(stack.Back())
		}
	}
	ans := 0
	for stack.Len() > 0 {
		ans += stack.Front().Value.(int)
		stack.Remove(stack.Front())
	}
	return ans
}

func main() {
	ops := []string{"5", "-2", "4", "C", "D", "9", "+", "+"}
	fmt.Println(calPoints(ops))
}
