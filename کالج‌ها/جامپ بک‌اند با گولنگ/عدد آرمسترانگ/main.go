package main

import (
    "bufio"
    "fmt"
    "math"
    "os"
    "strconv"
    "unicode"
)

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    scanner.Scan()
    s := scanner.Text()

    if s == "" {
        fmt.Print("YES")
        return
    }

    numbers := make([]int, 0)
    temp := 0

    for index, character := range s {
        if unicode.IsDigit(character) {
            digit, _ := strconv.Atoi(string(character))
            temp = temp*10 + digit
        }

        if index == len(s)-1 || !unicode.IsDigit(character) {
            if temp != 0 {
                numbers = append(numbers, temp)
                temp = 0
            }
        }
    }

    sum := 0
    armSum := 0

    for _, number := range numbers {
        sum += number
    }

    sumString := strconv.Itoa(sum)
    lenSum := len(sumString)

    for _, digit := range sumString {
        digit, _ := strconv.Atoi(string(digit))
        armSum += int(math.Pow(float64(digit), float64(lenSum)))
    }

    if sum == armSum {
        fmt.Print("YES")
    } else {
        fmt.Print("NO")
    }
}
