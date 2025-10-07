package main

import (
    "encoding/json"
    "errors"
    "fmt"
    "math"
    "net/http"
    "strconv"
    "strings"
)

type Server struct {
    host string
    port int
}

func NewServer(port string) *Server {
    portInt, err := strconv.Atoi(port)
    if err != nil {
        panic(err)
    }

    newServer := Server{"localhost", portInt}
    return &newServer
}

func (s *Server) Start() {
    http.HandleFunc("/add", add)
    http.HandleFunc("/sub", subtract)
    err := http.ListenAndServe(fmt.Sprintf("%s:%d", s.host, s.port), nil)
    if err != nil {
        fmt.Println("Error:", err)
    }
}

func add(w http.ResponseWriter, r *http.Request) {
    result := map[string]string{
        "result": "",
        "error":  "",
    }

    w.Header().Set("Content-Type", "application/json")

    numbers, err := checkNumbers(r)
    if err != nil {
        result["error"] = err.Error()

        w.WriteHeader(http.StatusBadRequest)
        json.NewEncoder(w).Encode(result)
        return
    }

    sumOfNumbers, err := sum(numbers)
    if err == nil {
        result["result"] = fmt.Sprintf("The result of your query is: %d", sumOfNumbers)
        w.WriteHeader(http.StatusOK)
    } else {
        result["error"] = err.Error()
        w.WriteHeader(http.StatusBadRequest)
    }

    json.NewEncoder(w).Encode(result)
}

func subtract(w http.ResponseWriter, r *http.Request) {
    result := map[string]string{
        "result": "",
        "error":  "",
    }

    w.Header().Set("Content-Type", "application/json")

    numbers, err := checkNumbers(r)
    if err != nil {
        result["error"] = err.Error()

        w.WriteHeader(http.StatusBadRequest)
        json.NewEncoder(w).Encode(result)
        return
    }

    subOfNumbers, err := sub(numbers)
    if err == nil {
        result["result"] = fmt.Sprintf("The result of your query is: %d", subOfNumbers)
        w.WriteHeader(http.StatusOK)
    } else {
        result["error"] = err.Error()
        w.WriteHeader(http.StatusBadRequest)
    }

    json.NewEncoder(w).Encode(result)
}

func sum(numbers []int) (int, error) {
    summation := 0

    for _, number := range numbers {
        if checkOverflow(number, summation) {
            return 0, errors.New("Overflow")
        }

        summation += number
    }

    return summation, nil
}

func sub(numbers []int) (int, error) {
    subtraction := numbers[0]

    for _, number := range numbers[1:] {
        if checkOverflow(-number, subtraction) {
            return 0, errors.New("Overflow")
        }

        subtraction -= number
    }

    return subtraction, nil
}

func checkNumbers(r *http.Request) ([]int, error) {
    numbersStr := r.URL.Query().Get("numbers")

    if numbersStr == "" {
        return nil, errors.New("'numbers' parameter missing")
    }

    numbers := strings.Split(numbersStr, `,`)

    integers := make([]int, len(numbers))
    for i, item := range numbers {
        num, err := strconv.Atoi(item)
        if err != nil {
            return nil, err
        }
        integers[i] = num
    }

    return integers, nil
}

func checkOverflow(num, sum int) bool {
    if num > 0 && sum >= math.MaxInt64-num {
        return true
    }
    if num < 0 && sum <= math.MinInt64-num {
        return true
    }
    return false
}

func main() {
    newServer := NewServer("8000")
    newServer.Start()
}
