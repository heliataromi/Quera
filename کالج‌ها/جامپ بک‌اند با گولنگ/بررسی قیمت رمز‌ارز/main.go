package main

import (
    "encoding/json"
    "errors"
    "io"
    "maps"
    "net/http"
    "slices"
    "strings"
)

func GetExchangeRate(source, destination string) (string, error) {
    client := &http.Client{}
    url := "http://localhost:4001/rates"

    params := map[string]string{
        "srcCurrency": strings.ToLower(source),
        "dstCurrency": strings.ToLower(destination),
    }

    if destination == "" {
        params["dstCurrency"] = "rls"
    }

    req, err := http.NewRequest("GET", url, nil)
    if err != nil {
        return "", err
    }

    q := req.URL.Query()

    for key, value := range params {
        q.Add(key, value)
    }

    req.URL.RawQuery = q.Encode()

    resp, err := client.Do(req)
    if err != nil {
        return "", err
    }
    defer resp.Body.Close()

    body, err := io.ReadAll(resp.Body)
    if err != nil {
        return "", err
    }
    
    var result struct {
        Status string                       `json:"status"`
        Stats  map[string]map[string]string `json:"stats"`
    }

    err = json.Unmarshal(body, &result)
    if err != nil {
        return "", err
    }
    print(result.Status)
    if result.Status != "OK" {
        return "", errors.New(result.Status)
    }

    value := slices.Collect(maps.Values(result.Stats))[0]["latest"]
    print(maps.Values(result.Stats))
    return value, nil
}
