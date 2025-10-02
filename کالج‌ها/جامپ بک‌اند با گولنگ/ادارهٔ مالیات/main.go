package main

import "fmt"

func main() {
	var (
		p   int
		tax = 0
	)
	fmt.Scanf("%d", &p)

	if p > 0 {
		tax += min(p, 100) * 5 / 100
		p -= min(p, 100)
	}

	if p > 0 {
		tax += min(p, 400) * 10 / 100
		p -= min(p, 400)
	}

	if p > 0 {
		tax += min(p, 500) * 15 / 100
		p -= min(p, 500)
	}

	if p > 0 {
		tax += p * 20 / 100
	}

	fmt.Print(tax)
}
