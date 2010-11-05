import threading
import cgi
import os
import random
import string
import time
import httplib	#http://docs.python.org/library/httplib.html
import urllib	#http://docs.python.org/library/urllib.html
import pickle	#http://docs.python.org/library/pickle.html
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SimpleHTTPServer
import pkg_resources

#import pdb

semaphore = None
keepGoing = 0
atom3Model = None
receivedData = None
server = None
port = -1
proxy_url = "localhost:12345"
proxy_path = "/"

staticResourcesToCopyIntoCwd = ["client.html","jquery-1.4.3.min.js","DChartsDebugListenerClient.js"]

class SimpleHTTPPostProxyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_POST(self):
		global proxy_url, proxy_path
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

#FIXME: ew, why are we using threads here? 
class SimpleHTTPPOSTProxyServerThread(threading.Thread):
	def run(self):
		global server, port, keepGoing
		server = HTTPServer(('', port), SimpleHTTPPostProxyHandler)
		server.timeout = 1 # 1s timeout
		while keepGoing:
			server.handle_request()
		server.socket.close()  # socket can now be re-used
		print 'stopped SimpleHTTPPOSTProxyServer'

def startServer(_port,_proxy_url):
	global port, proxy_url, keepGoing, semaphore
	port = _port
	proxy_url = _proxy_url
	keepGoing = 1
	semaphore = threading.Semaphore()
	print 'starting SimpleHTTPPOSTProxyServer...'	
	SimpleHTTPPOSTProxyServerThread().start()
	print 'started SimpleHTTPPOSTProxyServer...'	

	#copy the client html file into the current working directory so that we can serve it
	for resource in staticResourcesToCopyIntoCwd:
		resourceStr = pkg_resources.resource_string(__name__,resource)
		tmp = open(resource,"w")
		tmp.write(resourceStr);
		tmp.close()

def stopServer():
	global keepGoing
	keepGoing = 0
	print 'stopping SimpleHTTPPOSTProxyServer...'


def isServerRunning():
	global keepGoing
	return keepGoing

def main():
	startServer(8000,"localhost:12345")

if __name__ == "__main__":
	main()
