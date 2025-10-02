package main

import (
    "math"
    "strconv"
)

type FilterFunc func(int) bool
type MapperFunc func(int) int

func IsSquare(x int) bool {
    intSqrt := int(math.Sqrt(float64(x)))
    if intSqrt*intSqrt == x {
        return true
    }
    return false
}

func IsPalindrome(x int) bool {
    xString := strconv.Itoa(Abs(x))
    n := len(xString)

    reverse := ""
    for i := n - 1; i >= 0; i-- {
        reverse += xString[i : i+1]
    }

    if xString == reverse {
        return true
    }
    return false
}

func Abs(num int) int {
    if num < 0 {
        return -num
    }
    return num
}

func Cube(num int) int {
    return num * num * num
}

func Filter(input []int, f FilterFunc) []int {
    newSlice := make([]int, 0, len(input))

    for _, x := range input {
        if f(x) {
            newSlice = append(newSlice, x)
        }
    }

    return newSlice
}

func Map(input []int, m MapperFunc) []int {
    newSlice := make([]int, 0, len(input))

    for _, x := range input {
        newSlice = append(newSlice, m(x))
    }

    return newSlice
}
