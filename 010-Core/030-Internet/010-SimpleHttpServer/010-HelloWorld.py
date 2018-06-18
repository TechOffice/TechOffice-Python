import http.server
import socketserver

port = 8000

handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", port), handler) 
print("serving at port", port)
httpd.serve_forever()