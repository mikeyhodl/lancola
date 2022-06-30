# import http.server
# import socketserver

# PORT = 5500
# host = "localhost"
# url = f"http://{host}:{port}"

# Handler = http.server.SimpleHTTPRequestHandler

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()

import sys
import time
import threading
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

host = "localhost"
port = 5500
url = f"http://{host}:{port}"


def start_server():
    server_address = (host, port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()

threading.Thread(target=start_server).start()
webbrowser.open(url)

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)