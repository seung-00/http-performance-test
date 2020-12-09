const readline = require('readline');
const mysql = require('mysql');
const http = require('http');
const url = require('url');

const connectionHash = {
  nativeConnection: {
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'test_db',
  },
  vmConnection: {
    host: '192.168.27.129',
    user: 'test',
    password: 'test',
    database: 'vm_db',
  },
  containerConnection: {
    host: 'db_mysql',
    user: 'root',
    password: 'root',
    database: 'container_db',
  },
};

const parseJson = (res) => {
  res.writeHead(200, { 'Content-Type': 'application/json' });
  const objJson = require('../test.json');
  const testJson = JSON.stringify(objJson);
  res.end(testJson);
};

const parseDB = (connConfig, res) => {
  res.writeHead(200, { 'Content-Type': 'application/json' });

  let con = mysql.createConnection(connConfig);

  con.connect((err) => {
    if (err) throw err;
  });

  con.query('SELECT * from Users', (error, rows, fields) => {
    if (error) throw error;
    const testJson = JSON.stringify(rows[0]);
    // console.log(testJson);
    res.end(testJson);
  });

  con.end();
};

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question(
  `put server's enviroment\t 1: native, 2: vmware, 3: docker\n`,
  (answer) => {
    run(answer);
    rl.close();
  }
);

const run = (env) => {
  console.log('node server is running...');
  let connConfig;
  switch (env) {
    case '1':
      connConfig = connectionHash['nativeConnection'];
      break;

    case '2':
      connConfig = connectionHash['vmConnection'];
      break;

    case '3':
      connConfig = connectionHash['containerConnection'];
      break;
  }
  http
    .createServer((req, res) => {
      const path = url.parse(req.url, true).pathname;

      if (req.method === 'GET') {
        if (path === '/json') {
          parseJson(res);
        } else if (path === '/db') {
          parseDB(connConfig, res);
        } else {
          res.statusCode = 404;
          res.end('no adresss');
        }
      }
    })
    .listen(8081);
};
