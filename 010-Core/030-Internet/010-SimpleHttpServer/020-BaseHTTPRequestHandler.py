import http.server

class Handler(http.server.BaseHTTPRequestHandler):
	
	def do_GET(self):
		self.send_response(200)
		self.send_header("content-type", "text/html");
		self.end_headers();
		self.wfile.write(bytes("<html><body><h1>Testing</h1></body></html>", "utf-8"));
		self.wfile.flush()
		
	def do_POST(self):
		print("incoming http:" + self.path);
		self.send_response(200)
		self.send_header("content-type", "text/html");
		self.end_headers();
		self.wfile.write(btyes("<html><body><h1>Testing</h1></body></html>","utf-8"));
		self.wfile.flush()
		
httpd = http.server.HTTPServer(("", 8000), Handler);
httpd.serve_forever()