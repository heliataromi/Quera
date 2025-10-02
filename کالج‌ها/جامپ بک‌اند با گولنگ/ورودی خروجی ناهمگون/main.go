package main

import (
    "sync/atomic"
    "time"
)

type FutureResult struct {
    Done       atomic.Bool
    ResultChan chan string
    // TODO
}

type Task func() string

func Async(t Task) *FutureResult {
    fResult := &FutureResult{ResultChan: make(chan string, 1)}

    go func() {
        result := t()
        fResult.ResultChan <- result
        fResult.Done.Store(true)
    }()

    return fResult
}

func AsyncWithTimeout(t Task, timeout time.Duration) *FutureResult {
    fResult := &FutureResult{ResultChan: make(chan string, 1)}

    go func() {
        resultChan := make(chan string, 1)

        go func() {
            result := t()
            resultChan <- result
        }()

        select {
        case result := <-resultChan:
            fResult.ResultChan <- result
            fResult.Done.Store(true)

        case <-time.After(timeout):
            fResult.ResultChan <- "timeout"
        }
    }()

    return fResult
}

func (fResult *FutureResult) Await() string {
    result := <-fResult.ResultChan
    return result
}

func CombineFutureResults(fResults ...*FutureResult) *FutureResult {
    combinedResult := &FutureResult{ResultChan: make(chan string, len(fResults))}

    go func() {
        for _, fResult := range fResults {
            result := <-fResult.ResultChan
            combinedResult.ResultChan <- result
        }
        combinedResult.Done.Store(true)
    }()

    return combinedResult
}
