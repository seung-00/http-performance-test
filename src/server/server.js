const mysql = require("mysql"),
  http = require("http"),
  url = require("url");

const parseJson = (res) => {
  res.writeHead(200, { "Content-Type": "application/json" });
  const objJson = require("./test.json");
  const testJson = JSON.stringify(objJson);
  res.end(testJson);
};

const parseDB = (res) => {
  res.writeHead(200, { "Content-Type": "application/json" });
  const native_connection = {
    host: "localhost",
    user: "root",
    password: "root",
    database: "test_db",
  };

  // const container_connection = {
  //   host: 'db_mysql',
  //   user: 'root',
  //   post: 3306,
  //   password: 'root',
  //   database: 'container_db'
  // }

  let con = mysql.createConnection(container_connection);

  con.connect((err) => {
    if (err) throw err;
    console.log("Connected!");
  });

  con.query("SELECT * from Users", (error, rows, fields) => {
    if (error) throw error;
    const testJson = JSON.stringify(rows[0]);
    console.log(testJson);
    res.end(testJson);
  });

  con.end();
};

http
  .createServer((req, res) => {
    const path = url.parse(req.url, true).pathname;

    if (req.method === "GET") {
      if (path === "/json") {
        parseJson(res);
      } else if (path === "/db") {
        parseDB(res);
      } else {
        res.statusCode = 404;
        res.end("no adresss");
      }
    }
  })
  .listen(8081);
