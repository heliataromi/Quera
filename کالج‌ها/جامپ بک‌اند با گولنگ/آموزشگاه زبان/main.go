package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var n int
	fmt.Scanln(&n)

	scanner := bufio.NewScanner(os.Stdin)

	for i := 0; i < n; i++ {
		scanner.Scan()
		instructorName := scanner.Text()

		scanner.Scan()
		scoreStrings := strings.Fields(scanner.Text())

		var totalScore int = 0
		var numScores int = 0

		for _, scoreStr := range scoreStrings {
			score, _ := strconv.Atoi(scoreStr)
			totalScore += score
			numScores++
		}

		var averageScore float64
		if numScores > 0 {
			averageScore = float64(totalScore) / float64(numScores)
		} else {
			averageScore = 0
		}

		var evaluation string
		if averageScore >= 80 {
			evaluation = "Excellent"
		} else if averageScore >= 60 {
			evaluation = "Very Good"
		} else if averageScore >= 40 {
			evaluation = "Good"
		} else {
			evaluation = "Fair"
		}

		fmt.Println(instructorName, evaluation)
	}
}
