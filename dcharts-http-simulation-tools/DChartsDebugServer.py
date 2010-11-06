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

#import pdb

semaphore = None
keepGoing = 0
atom3Model = None
receivedData = None
server = None
port = -1
atom3i = None

#{'Hyperedge': [<Hyperedge.Hyperedge instance at 0xb73ef6c>], 'Orthogonal': [], 'Composite': [<Composite.Composite instance at 0xb63660c>], 'ASG_DCharts': [], 'contains': [<contains.contains instance at 0xb735d6c>], 'ASG_DChartsSCXMLGenerator': [], 'Class_0': [], 'orthogonality': [], 'Server': [], 'connection': [], 'visual_settings': [], 'Basic': [<Basic.Basic instance at 0xb735d8c>, <Basic.Basic instance at 0xb735dac>], 'Port': [], 'History': []}


class DChartsDebugServer(BaseHTTPRequestHandler):


	def _getStateById(self,nodeList,id):
		stateClasses = ('Composite','Basic','Orthogonal');

		allStates = reduce( lambda l1,l2: l1 + l2, [nodeList[stateClass] for stateClass in stateClasses])
		singleStateList = filter(lambda s: id == s.name.toString(), allStates)
		if singleStateList:
			return singleStateList[0]
		else:
			print("State not found with id %s" % id)
			#pdb.set_trace()
			return None


	def _highlightOrLowlightState(self,parsed_data,highlight):
                global atom3Model

		stateid = parsed_data['stateid'][0]

		print("Highlighting state %s" % stateid)
		if atom3Model:
			#look up state by its id
			nodelist=atom3Model.listNodes

			#highlight him
			state = self._getStateById(nodelist,stateid)
			#state might not be found, as scxml-js compiler adds in some states that are not found in the original model (e.g. explicit initial states)
			if state:
				state.graphObject_.HighLight(highlight)

	def reply(self):
		self.send_response(200)
		self.end_headers()

	def do_GET(self):
		pass
			
	def do_POST(self):
                global atom3Model

		print "HANDLING POST"
		contentlength = string.atoi(self.headers.getheader('content-length')) 
		#Retrieve and parse transmission
		post_data = self.rfile.read(contentlength)
		print "read post data - about to parse"
  		parsed_data = cgi.parse_qs(post_data)
		print "RECEIVED POST REQUEST WITH DATA: "+str(parsed_data)

		#Handle the transmitted request, e.g.:
		#if parsed_data['command'][0] == 'exec' :
		#	exec(parsed_data['code'][0])

		if parsed_data['command'][0] == 'enter':
			self._highlightOrLowlightState(parsed_data,1)

		elif parsed_data['command'][0] == 'exit':
			self._highlightOrLowlightState(parsed_data,0)

		#TODO: transitions as well
		elif parsed_data['command'][0] == 'clear':
			nodelist=atom3Model.listNodes
			for nodeType in nodeList:
				for node in nodeType:
					node.graphObject_.HighLight(0)

		else:
			pass

		self.reply()
		

#FIXME: ew, why are we using threads here? 
class DChartsDebugServerThread(threading.Thread):
	def run(self):
		global server, port, keepGoing
		server = HTTPServer(('', port), DChartsDebugServer)
		server.timeout = 1 # 1s timeout
		while keepGoing:
			server.handle_request()
		server.socket.close()  # socket can now be re-used
		print 'stopped DChartsDebugServer'

def startServer(_atom3i, _atom3Model,_port):
	global atom3i, atom3Model, port, keepGoing, semaphore
	atom3i = _atom3i
	atom3Model = _atom3Model
	port = _port
	keepGoing = 1
	semaphore = threading.Semaphore()
	print 'starting DChartsDebugServer...'	
	DChartsDebugServerThread().start()
	print 'started DChartsDebugServer...'	


def stopServer():
	global keepGoing
	keepGoing = 0
	print 'stopping DChartsDebugServer...'


def isServerRunning():
	global keepGoing
	return keepGoing

def main():
	startServer(None, None, 12345)

if __name__ == "__main__":
	main()
