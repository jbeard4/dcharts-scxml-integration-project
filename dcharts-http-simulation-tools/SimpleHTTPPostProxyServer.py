import httplib, urllib
import SimpleHTTPServer
import SocketServer
import cgi
import string

port = 8000

proxy_url = "localhost:12345"
#proxy_url = "localhost:8001"
proxy_path = "/"

class SimpleHTTPPostProxyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_POST(self):
		contentlength = string.atoi(self.headers.getheader('content-length')) 
		#Retrieve and parse transmission
		post_data = self.rfile.read(contentlength)
		print "read post data - about to parse"
  		#parsed_data = cgi.parse_qs(post_data)
		#print(parsed_data)

		#set up new request to the application server
		headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
		conn = httplib.HTTPConnection(proxy_url)
		conn.request("POST", proxy_path, post_data, headers)
		response = conn.getresponse()
		print response.status, response.reason
		data = response.read()
		conn.close()

		#send response back
		self.send_response(response.status)


if __name__ == "__main__":
	httpd = SocketServer.TCPServer(("", port), SimpleHTTPPostProxyHandler)

	print "serving at port", port
	httpd.serve_forever()

