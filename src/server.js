const http = require('http');
const url = require('url');

http.createServer((req, res) => {
  const path = url.parse(req.url, true).pathname;
  if (req.method === 'GET') {
    if (path === '/node') {
      res.writeHead(200,{'Content-Type':'application/json'});
      let test = {'key':1};
      let testJson = JSON.stringify(test);
      res.end(testJson);
    } else {
      res.statusCode = 404;
      res.end('no adresss');
    }
  }
}).listen(8080);
