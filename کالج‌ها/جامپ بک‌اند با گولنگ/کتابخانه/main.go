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

    books := make(map[int]string)

    for i := 0; i < n; i++ {
        scanner.Scan()
        command := strings.Fields(scanner.Text())

        if command[0] == "ADD" {
            isbn, _ := strconv.Atoi(command[1])
            book := command[2]

            books[isbn] = book
        } else if command[0] == "REMOVE" {
            isbn, _ := strconv.Atoi(command[1])

            delete(books, isbn)
        }
    }

    isbns := make([]int, 0, len(books))
    for isbn := range books {
        isbns = append(isbns, isbn)
    }

    sort.Slice(isbns, func(i, j int) bool {
        isbnI := isbns[i]
        isbnJ := isbns[j]
        nameI := books[isbnI]
        nameJ := books[isbnJ]

        if nameI != nameJ {
            return nameI < nameJ
        }

        return isbnI < isbnJ
    })

    for _, isbn := range isbns {
        fmt.Printf("%d\n", isbn)
    }
}
