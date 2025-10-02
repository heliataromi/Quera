package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)

func main() {
    scanner := bufio.NewScanner(os.Stdin)

    scanner.Scan()
    n, _ := strconv.Atoi(scanner.Text())

    codes := make(map[string]string)

    for i := 0; i < n; i++ {
        scanner.Scan()
        line := strings.Fields(scanner.Text())

        codes[line[1]] = line[0]
    }

    scanner.Scan()
    q, _ := strconv.Atoi(scanner.Text())

    for i := 0; i < q; i++ {
        scanner.Scan()
        phoneNumber := scanner.Text()

        country, status := codes[phoneNumber[:3]]
        if !status {
            fmt.Println("Invalid Number")
        } else {
            fmt.Println(country)
        }
    }
}
