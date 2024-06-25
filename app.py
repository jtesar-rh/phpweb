# Python 3 server example
"""Module doc
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
HOST_NAME = "0.0.0.0"
SERVER_PORT = 8080
class MyServer(BaseHTTPRequestHandler):
    """Class docs
    """
    def do_GET(self):
        """Calculates the area of a rectangle.

          This function takes the length and width of a rectangle as arguments
          and returns the calculated area.

          Args:
              length: The length of the rectangle (float).
              width: The width of the rectangle (float).

          Returns:
              The area of the rectangle (float).
          """
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("Hello World!", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((HOST_NAME, SERVER_PORT), MyServer)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
