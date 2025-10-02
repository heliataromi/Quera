package main

func StartDecipher(senderChan chan string, decipherer func(encrypted string) string) chan string {
    decipheredChan := make(chan string, 5)

    go func() {
        for encryptedMessage := range senderChan {
            decipheredChan <- decipherer(encryptedMessage)
        }
    }()

    return decipheredChan
}
