package main

import (
    "fmt"
    "sort"
    "sync"
    "testing"
    "time"

    "github.com/stretchr/testify/assert"
)

func TestGameCreation(t *testing.T) {
    g, err := NewGame([]int{})
    assert.Nil(t, err)
    assert.NotNil(t, g)
}

func TestAddMap(t *testing.T) {
    g, err := NewGame([]int{1, 2, 3})
    assert.Nil(t, err)

    _, err = g.GetMap(1)
    assert.Nil(t, err)
}

func TestAddInvalidMap(t *testing.T) {
    g, err := NewGame([]int{-1, 2, 3})
    assert.Error(t, err)

    if g != nil {
        _, err = g.GetMap(-1)
        assert.Error(t, err)
    }
}

func TestAddPlayer(t *testing.T) {
    g, err := NewGame([]int{1, 2, 3})
    assert.Nil(t, err)

    err = g.ConnectPlayer("Cyn")
    assert.Nil(t, err)
}

func TestConcurrentConnection(t *testing.T) {
    g, err := NewGame([]int{1, 2, 3})
    assert.Nil(t, err)

    var errorsList []error
    var m sync.Mutex
    var wg sync.WaitGroup
    for i := 0; i < 10; i++ {
        wg.Add(1)
        go func(i int) {
            defer wg.Done()
            err := g.ConnectPlayer("username")
            m.Lock()
            defer m.Unlock()
            errorsList = append(errorsList, err)
        }(i)
    }
    wg.Wait()

    expected := []error{nil}
    for i := 0; i < 9; i++ {
        expected = append(expected, g.ConnectPlayer("username"))
    }

    assert.EqualValues(t, expected, errorsList)
}

func TestGetPlayer(t *testing.T) {
    g, err := NewGame([]int{1, 2, 3})
    assert.Nil(t, err)

    err = g.ConnectPlayer("Cyn")
    assert.Nil(t, err)

    p, err := g.GetPlayer("CyN")
    assert.Nil(t, err)
    assert.NotNil(t, p)
}

func TestPlayerSendMessageInvalid(t *testing.T) {
    g, err := NewGame([]int{1, 2, 3})
    assert.Nil(t, err)

    err = g.ConnectPlayer("Cyn")
    assert.Nil(t, err)

    p, err := g.GetPlayer("CyN")
    assert.Nil(t, err)
    assert.NotNil(t, p)

    err = p.SendMessage("Hey guys")
    assert.Error(t, err)
}

func TestPlayerSendMessageInvalid2(t *testing.T) {
    g, err := NewGame([]int{1, 2, 3})
    assert.Nil(t, err)

    err = g.ConnectPlayer("Cyn")
    assert.Nil(t, err)

    p, err := g.GetPlayer("CyN")
    assert.Nil(t, err)
    assert.NotNil(t, p)

    err = p.SendMessage("")
    assert.Error(t, err)
}

func TestPlayerReadMessage(t *testing.T) {
    g, err := NewGame([]int{1, 2, 3})
    assert.Nil(t, err)

    err = g.ConnectPlayer("Cyn")
    assert.Nil(t, err)
    err = g.ConnectPlayer("Listener")
    assert.Nil(t, err)

    p, err := g.GetPlayer("CyN")
    assert.Nil(t, err)
    assert.NotNil(t, p)

    p2, err := g.GetPlayer("lIsteneR")
    assert.Nil(t, err)
    assert.NotNil(t, p2)

    err = g.SwitchPlayerMap("CyN", 1)
    assert.Nil(t, err)
    err = g.SwitchPlayerMap("listeneR", 1)
    assert.Nil(t, err)

    err = p.SendMessage("Hey guys")
    assert.Nil(t, err)

    listenChan := p2.GetChannel()
    assert.Equal(t, "Cyn says: Hey guys", <-listenChan)
}

func TestPlayerSwitchMap(t *testing.T) {
    g, err := NewGame([]int{1, 2, 3})
    assert.Nil(t, err)

    err = g.ConnectPlayer("Cyn")
    assert.Nil(t, err)
    err = g.ConnectPlayer("Listener")
    assert.Nil(t, err)

    p, err := g.GetPlayer("CyN")
    assert.Nil(t, err)
    assert.NotNil(t, p)

    p2, err := g.GetPlayer("lIsteneR")
    assert.Nil(t, err)
    assert.NotNil(t, p2)

    err = g.SwitchPlayerMap("CyN", 1)
    assert.Nil(t, err)
    err = g.SwitchPlayerMap("listeneR", 1)
    assert.Nil(t, err)
    err = g.SwitchPlayerMap("CyN", 2)
    assert.Nil(t, err)

    err = p.SendMessage("Hey guys")
    assert.Nil(t, err)

    select {
    case <-p2.GetChannel():
        t.Fatalf("Message sent to incorrect map")
    default:
    }
}

func TestMulti(t *testing.T) {
    g, err := NewGame([]int{1, 2, 3})
    assert.Nil(t, err)

    err = g.ConnectPlayer("Cyn")
    assert.Nil(t, err)
    err = g.ConnectPlayer("1stListener")
    assert.Nil(t, err)
    err = g.ConnectPlayer("2Cyn")
    assert.Nil(t, err)
    err = g.ConnectPlayer("2ndListener")
    assert.Nil(t, err)

    p, err := g.GetPlayer("CyN")
    assert.Nil(t, err)
    assert.NotNil(t, p)

    p1, err := g.GetPlayer("1stListener")
    assert.Nil(t, err)
    assert.NotNil(t, p)

    p2, err := g.GetPlayer("2cyn")
    assert.Nil(t, err)
    assert.NotNil(t, p2)

    p3, err := g.GetPlayer("2ndListener")
    assert.Nil(t, err)
    assert.NotNil(t, p2)

    err = g.SwitchPlayerMap("CyN", 1)
    assert.Nil(t, err)
    err = g.SwitchPlayerMap("1stlisteneR", 1)
    assert.Nil(t, err)
    err = g.SwitchPlayerMap("2cYn", 2)
    assert.Nil(t, err)
    err = g.SwitchPlayerMap("2ndlisteneR", 2)
    assert.Nil(t, err)

    stringList1st, stringList2nd := []string{
        "Hey Guys", "How are you", "This is the 1st map",
    }, []string{
        "Hey Guys", "How are you", "This is the 2nd map",
    }

    err = p.SendMessage(stringList1st[0])
    assert.Nil(t, err)
    err = p1.SendMessage(stringList1st[1])
    assert.Nil(t, err)
    err = p.SendMessage(stringList1st[2])
    assert.Nil(t, err)

    for _, msg := range stringList2nd {
        err = p2.SendMessage(msg)
        assert.Nil(t, err)
    }

    expected1st := []string{
        "Cyn says: Hey Guys", "Cyn says: This is the 1st map",
    }

    expected2nd := []string{
        "2cyn says: Hey Guys", "2cyn says: How are you", "2cyn says: This is the 2nd map",
    }

    actual1, actual2 := make([]string, 0, 3), make([]string, 0, 3)

    safeMargin := 300 * time.Millisecond
    tch := time.After(safeMargin)
    for {
        done := false
        select {
        case msg := <-p1.GetChannel():
            actual1 = append(actual1, msg)
        case msg := <-p3.GetChannel():
            actual2 = append(actual2, msg)
        case <-tch:
            done = true
        }
        if done {
            break
        }
    }

    assert.EqualValues(t, expected1st, actual1)
    assert.EqualValues(t, expected2nd, actual2)
}

func generateFakeUsernames(n int) []string {
    result := make([]string, 0, n)
    for i := 0; i < n; i++ {
        result = append(result, fmt.Sprintf("cyn%d", i))
    }
    return result
}

func generateFakeMessages(n int) []string {
    result := make([]string, 0, n)
    for i := 0; i < n; i++ {
        if i == 0 {
            result = append(result, "Hello Everyone")
        }
        if i%2 == 0 {
            result = append(result, "Hey guys")
        }
        if i%2 != 0 {
            result = append(result, "Good bye")
        }
    }
    return result
}

func TestConcurrentMessageSingleMap(t *testing.T) {
    g, err := NewGame([]int{1, 2, 3})
    assert.Nil(t, err)

    err = g.ConnectPlayer("cyn")
    assert.Nil(t, err)
    err = g.ConnectPlayer("cyn2")
    assert.Nil(t, err)
    err = g.ConnectPlayer("cyn3")
    assert.Nil(t, err)

    p1, err := g.GetPlayer("cyn")
    assert.Nil(t, err)
    p2, err := g.GetPlayer("cyn2")
    assert.Nil(t, err)
    p3, err := g.GetPlayer("cyn3")
    assert.Nil(t, err)

    err = g.SwitchPlayerMap(p1.GetName(), 1)
    assert.Nil(t, err)
    err = g.SwitchPlayerMap(p2.GetName(), 1)
    assert.Nil(t, err)
    err = g.SwitchPlayerMap(p3.GetName(), 1)
    assert.Nil(t, err)

    numberOfFakeMessages := 2
    messages := generateFakeMessages(numberOfFakeMessages)
    var wg sync.WaitGroup

    var expectedMessages []string
    for i := 0; i < len(messages); i++ {
        expectedMessages = append(expectedMessages, fmt.Sprintf("%s says: %s", "Cyn", messages[i]))
        expectedMessages = append(expectedMessages, fmt.Sprintf("%s says: %s", "Cyn2", messages[i]))

        safeMargin := 100 * time.Millisecond
        time.Sleep(safeMargin)

        wg.Add(1)
        go func(i int) {
            defer wg.Done()
            p1.SendMessage(messages[i])
        }(i)

        wg.Add(1)
        go func(i int) {
            defer wg.Done()
            p2.SendMessage(messages[i])
        }(i)
    }

    wg.Wait()

    var actualMessages []string
    var m sync.Mutex

    wg.Add(1)
    go func() {
        defer wg.Done()
        for {
            select {
            case msg := <-p3.GetChannel():
                m.Lock()
                actualMessages = append(actualMessages, msg)
                m.Unlock()
            case <-time.After(500 * time.Millisecond):
                return
            }
        }
    }()
    wg.Wait()

    m.Lock()
    defer m.Unlock()

    sort.Strings(actualMessages)
    sort.Strings(expectedMessages)

    assert.EqualValues(t, expectedMessages, actualMessages)
}
