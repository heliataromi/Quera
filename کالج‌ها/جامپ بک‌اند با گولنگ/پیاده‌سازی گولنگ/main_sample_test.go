package main

import (
	"testing"
)

func TestSample(t *testing.T) {
	q := NewQutex()
	q.Lock()
	q.Unlock()
}
