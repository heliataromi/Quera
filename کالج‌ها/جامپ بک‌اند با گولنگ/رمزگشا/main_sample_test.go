package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSampleDecipher(t *testing.T) {
	var receiver chan string
	var sender = make(chan string)
	go func() {
		receiver = StartDecipher(sender, func(encrypted string) string {
			var result string
			for _, v := range encrypted {
				if v == 'h' {
					result += "a"
				} else if v == 'a' {
					result += "h"
				} else {
					result += string(v)
				}
			}
			return result
		})
	}()

	sender <- "aello"
	assert.Equal(t, "hello", <-receiver)
}
