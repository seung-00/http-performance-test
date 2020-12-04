package main

import (
	"database/sql" 
	"log"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	_ "github.com/go-sql-driver/mysql"
)

var env int

func loadFile(fileName string) (string, error) {
	bytes, err := ioutil.ReadFile(fileName)
	if err != nil {
		return "", err
	}
	return string(bytes), nil
}

type Test struct {
	name   string
	value    int
}

func handleJson(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json; charset=utf-8")
	var body, _ = loadFile("../test.json")
	fmt.Fprintf(w, body)
}

func handleDB(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json; charset=utf-8")
	var conn string
	if env == 1 {
		conn = "root:root@tcp(localhost:3306)/test_db"
	} else if env == 2 {
		conn = "test:test@tcp(192.168.27.129:3306)/vm_db"
	} else if env == 3 {
		conn = "root:root@tcp(db_mysql:3306)/container_db"
	}
	db, err := sql.Open("mysql", conn)
	if err != nil {
    log.Fatal(err)
	}

	var name string
	var value int
	err = db.QueryRow("SELECT * from Users").Scan(&value, &name)

	if err != nil {
		log.Fatal(err)
	}
	data := make(map[string]interface{})
	data[name] = value
	jsonData, err := json.Marshal(data)	
	fmt.Fprintf(w, string(jsonData))
}

func main() {
	fmt.Print("put server's enviroment\t 1: native, 2: vmware, 3: docker\n")
	fmt.Scanf("%d", &env)
	fmt.Print("go server is running...")
	http.HandleFunc("/json", handleJson)
	http.HandleFunc("/db", handleDB)
	log.Fatal(http.ListenAndServe(":8083", nil))
}
