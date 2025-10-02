package main

import (
	"fmt"
	"strings"
)

func main() {
	var p, q int
	fmt.Scanf("%d %d", &p, &q)

	for i := 1; i <= q; i++ {
		if i%p == 0 {
			words := make([]string, i/p)
			for j := 0; j < i/p; j++ {
				words[j] = "Hope"
			}
			fmt.Println(strings.Join(words, " "))
		} else {
			fmt.Println(i)
		}
	}
}
