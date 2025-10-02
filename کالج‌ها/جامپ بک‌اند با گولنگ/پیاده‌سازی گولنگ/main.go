package main

type Qutex struct {
    locked  bool
    running chan bool
}

func NewQutex() *Qutex {
    return &Qutex{locked: false, running: make(chan bool, 1)}
}

func (q *Qutex) Lock() {
    q.locked = true
    q.running <- true
}

func (q *Qutex) Unlock() {
    if !q.locked {
        panic("unlock of unlocked Qutex")
    }

    <-q.running
    q.locked = false
}
