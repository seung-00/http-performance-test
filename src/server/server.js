const mysql = require("mysql");
const http = require("http");
const url = require("url");

const connection = mysql.createConnection({
  host: "localhost",
  user: "me",
  password: "secret",
  database: "my_db",
});

const parseJson = (res) => {
  res.writeHead(200, { "Content-Type": "application/json" });
  const objJson = require("./test.json");
  const testJson = JSON.stringify(objJson);
  res.end(testJson);
};

http
  .createServer((req, res) => {
    const path = url.parse(req.url, true).pathname;

    if (req.method === "GET") {
      if (path === "/json") {
        parseJson(res);
      } else if (path === "/db") {
      } else {
        res.statusCode = 404;
        res.end("no adresss");
      }

      // if (path === "/db") {
      //   res.writeHead(200, { "Content-Type": "application/json" });
      // }
    }
  })
  .listen(8081);
