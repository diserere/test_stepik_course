import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class AdvancedHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)
        if parsed.path == '/search':
            query = params.get('q', ['default'])[0]
            self._respond(200, f"Search query: {query}")
        else:
            self._respond(404, "Not Found")

    def do_POST(self):
        if self.path == '/api/data':
            length = int(self.headers.get('Content-Length', 0))
            data = json.loads(self.rfile.read(length).decode('utf-8'))
            self._respond(200, f"Received: {data}")
        else:
            self._respond(404, "Not Found")

    def _respond(self, code, msg):
        self.send_response(code)
        self.end_headers()
        self.wfile.write(msg.encode('utf-8'))

if __name__ == '__main__':
    HTTPServer(('localhost', 8000), AdvancedHandler).serve_forever()
