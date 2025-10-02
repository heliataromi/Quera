package main

import "fmt"

func ConvertToDigitalFormat(hour, minute, second int) string {
    s := fmt.Sprintf("%02d:%02d:%02d", hour, minute, second)
    return s
}

func ExtractTimeUnits(seconds int) (int, int, int) {
    hour := seconds / 3600
    minute := (seconds % 3600) / 60
    second := seconds % 3600 % 60
    return hour, minute, second
}
