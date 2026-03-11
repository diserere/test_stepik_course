"""Simple HTTP server with URL paths handling."""

import http.server
from urllib.parse import parse_qs, urlparse


class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    """Handle GET reauest."""

    def do_GET(self):
        # Parse the URL path and query parameters
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query_params = parse_qs(parsed_path.query)

        if path == "/":
            self.handle_root()
        elif path == "/hello":
            self.handle_hello(query_params)
        else:
            self.handle_not_found()

        # self.finish()

    def handle_root(self):
        """Handle root path."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        # self.send_header("Connection", "close")
        self.end_headers()
        response_content = b"<h1>Welcome to the Home Page!</h1>"
        self.wfile.write(response_content)

    def handle_hello(self, query_params: dict):
        """Handle /hello path."""
        # name = query_params.get('name', ['World'])[0] # Default to 'World' if name is not provided
        name = query_params.get(
            "name", ["World"]
        )  # Default to 'World' if name is not provided
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # response_content = f"<h1>Hello, {name}!</h1>".encode('utf-8')
        response_content = b""
        for n in name:
            response_content += f"<h1>Hello, {n}!</h1>".encode("utf-8")
        self.wfile.write(response_content)

    def handle_not_found(self):
        """Handle unexistent paths."""
        self.send_response(404)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        response_content = b"<h1>404 Not Found</h1>"
        self.wfile.write(response_content)


def run_server():
    """Run server, handle keyboard interrupt to stop."""
    PORT = 8000
    # Use ThreadingHTTPServer for better handling of multiple requests
    with http.server.HTTPServer(("", PORT), MyRequestHandler) as httpd:
        print(f"Serving at port {PORT}")
        print(f"Try visiting: http://localhost:{PORT}")
        print(f"Try visiting: http://localhost:{PORT}/hello?name=Alice")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()
            print("Server stopped.")


if __name__ == "__main__":
    run_server()
