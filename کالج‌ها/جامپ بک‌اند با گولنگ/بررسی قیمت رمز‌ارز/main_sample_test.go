package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
)

func startServer() {
	type stats struct {
		Latest string `json:"latest"`
	}

	type information struct {
		Status string           `json:"status"`
		Stats  map[string]stats `json:"stats"`
	}

	var datalist = make(map[string]information)

	f, err := os.Open("data.json")
	if err != nil {
		panic(err)
	}
	defer f.Close()

	err = json.NewDecoder(f).Decode(&datalist)
	if err != nil {
		panic(err)
	}

	http.HandleFunc("/rates", func(w http.ResponseWriter, r *http.Request) {
		src := r.URL.Query().Get("srcCurrency")
		dst := r.URL.Query().Get("dstCurrency")
		if info, ok := datalist[fmt.Sprintf("%s-%s", src, dst)]; ok {
			w.WriteHeader(http.StatusOK)
			w.Header().Set("Content-Type", "application/json")
			json.NewEncoder(w).Encode(info)
			return
		}

		w.WriteHeader(http.StatusBadRequest)
		w.Write([]byte("Invalid Requests"))
		return
	})

	log.Fatal(http.ListenAndServe(":4001", nil))
}

type sampleTestExchangeResponse struct {
	Status string                    `json:"status"`
	Stats  map[string]sampleTestStat `json:"stats"`
}

type sampleTestStat struct {
	Latest string `json:"latest"`
}

func TestSampleGetBTCtoRials(t *testing.T) {
	go startServer()
	time.Sleep(30 * time.Millisecond)
	result, err := GetExchangeRate("BTC", "")
	if err != nil {
		t.Errorf("No Errors Were Expected But Got %s", err.Error())
	}

	resp, err := http.DefaultClient.Get("http://localhost:4001/rates?srcCurrency=btc&dstCurrency=rls")
	if err != nil {
		t.Errorf("No Errors Were Expected But Got %s", err.Error())
	}
	defer resp.Body.Close()

	b, err := io.ReadAll(resp.Body)
	if err != nil {
		t.Errorf("No Errors Were Expected But Got %s", err.Error())
	}

	var response sampleTestExchangeResponse
	err = json.Unmarshal(b, &response)
	if err != nil {
		t.Errorf("No Errors Were Expected But Got %s", err.Error())
	}

	assert.Equal(t, response.Stats[fmt.Sprintf("%s-%s", "btc", "rls")].Latest, result)
}
