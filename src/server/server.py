import http.server

class HTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """HTTP 요청을 처리하는 클래스"""

    def do_GET(self):  # ❶
        """HTTP GET 요청을 처리한다."""
        self.route()

    def route(self):  # ❷
        """요청 URL의 path에 따라 요청을 처리할 함수를 중계한다."""
        if self.path == '/hello':
            self.hello()
        else:
            self.reponse_404_not_found()

    def hello(self):  # ❸
        """200 OK 상태 코드와 인삿말을 응답한다."""
        self.response(200, '안녕하세요?')

    def reponse_404_not_found(self):  # ❹
        """404 Not Found 상태 코드와 오류 메시지를 응답한다."""
        self.response(404, '요청하신 문서를 찾을 수 없습니다.')

    def response(self, status_code, body):  # ❺
        """응답 메시지를 전송한다."""
        # 상태 코드 전송
        self.send_response(status_code)

        # 헤더 전송
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # 본문 전송
        self.wfile.write(body.encode('utf-8'))

# 요청받을 주소 (요청을 감시할 주소)
ADDRESS = 'localhost', 8000

# 요청 대기하기
listener = http.server.HTTPServer(ADDRESS, HTTPRequestHandler)  # ❻
print(f'http://{ADDRESS[0]}:{ADDRESS[1]} 주소에서 요청 대기중...')
listener.serve_forever()  # ❼
