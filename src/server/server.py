from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.route()
        except Exception as e:
            self.send_response(400)
            print(e)

    def route(self):
        if self.path == '/python':
            self.test()
        else:
            self.send_response(404)

    def test(self):
        json_msg = json.dumps({'id': 1})
        self.response(200, json_msg)

    def response(self, status_code, body):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(body, 'utf-8'))

def run(address, server_class=HTTPServer, handler_class=HTTPRequestHandler):
    server_address = address
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    address = 'localhost', 8081
    run(address=address)