from http.server import BaseHTTPRequestHandler, HTTPServer
import pymysql
import json


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.route()
        except Exception as e:
            self.send_response(400)
            print(e)

    def route(self):
        if self.path == '/json':
            self.parse_json()
        elif self.path == '/db':
            self.parse_db()
        else:
            self.send_response(404)

    def parse_json(self):
        with open('../test.json') as json_file:
            json_data = json.load(json_file)
        json_msg = json.dumps(json_data)
        self.response(200, json_msg)

    def parse_db(self):
        if env == 1:
            connection = pymysql.connect(
                host='localhost',
                user='root',
                passwd='root',
                port=3306,
                db='test_db',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        elif env == 2:
            connection = pymysql.connect(
                host='192.168.27.129',
                user='test',
                passwd='test',
                port=3306,
                db='vm_db',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        elif env == 3:
            connection = pymysql.connect(
                host='db_mysql',
                user='root',
                passwd='root',
                port=3306,
                db='container_db',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        else:
            print("wrong env number")
            return

        try:
            with connection.cursor() as cursor:
                sql = "SELECT * from Users"
                cursor.execute(sql)
                result = cursor.fetchone()
                # print(result)
                json_msg = json.dumps(result)
                self.response(200, json_msg)

        except Exception as e:
            print(e)

        finally:
            connection.close()

    def response(self, status_code, body):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(body, 'utf-8'))


def run(address, server_class=HTTPServer, handler_class=HTTPRequestHandler):
    server_address = address
    httpd = server_class(server_address, handler_class)
    print("python server is running...")
    httpd.serve_forever()


if __name__ == "__main__":
    env = int(input("put server's enviroment\t 1: native, 2: vmware, 3: docker\n"))
    address = '', 8082
    run(address=address)
