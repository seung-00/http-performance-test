package main

import (
	"log"
    "fmt"
	"io/ioutil"
    "net/http"
)

func loadFile(fileName string) (string, error) {
	bytes, err := ioutil.ReadFile(fileName)
	if err != nil {
		return "", err
	}
	return string(bytes), nil
}

func handler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json; charset=utf-8")
	var body, _ = loadFile("test.json")
    fmt.Fprintf(w, body)
}

func main() {
    http.HandleFunc("/go", handler)
	log.Fatal(http.ListenAndServe(":8082", nil))
}