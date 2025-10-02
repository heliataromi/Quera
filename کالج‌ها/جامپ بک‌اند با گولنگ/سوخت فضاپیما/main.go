package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())

	pros := make(map[string]int)

	for i := 0; i < n; i++ {
		scanner.Scan()
		line := scanner.Text()

		parts := strings.Fields(line)

		name := parts[0]

		currentProgression := 2
		progressions := 0

		var currentNumbers []int

		for j, numStr := range parts[1:] {
			num, _ := strconv.Atoi(numStr)

			if j >= 2 {
				currentDifference := num - currentNumbers[j-1]

				if currentDifference == currentNumbers[j-1]-currentNumbers[j-2] {
					currentProgression += 1
				}

				if currentDifference != currentNumbers[j-1]-currentNumbers[j-2] || j == len(parts[1:])-1 {
					if currentProgression >= 3 {
						progressions += (currentProgression - 1) * (currentProgression - 2) / 2
						currentProgression = 2
					}
				}
			}

			currentNumbers = append(currentNumbers, num)
		}

		pros[name] = progressions
	}

	names := make([]string, 0, len(pros))
	for name := range pros {
		names = append(names, name)
	}

	sort.Slice(names, func(i, j int) bool {
		nameI := names[i]
		nameJ := names[j]
		countI := pros[nameI]
		countJ := pros[nameJ]

		if countI != countJ {
			return countI > countJ
		}

		return nameI < nameJ
	})

	for _, name := range names {
		fmt.Printf("%s %d\n", name, pros[name])
	}
}
