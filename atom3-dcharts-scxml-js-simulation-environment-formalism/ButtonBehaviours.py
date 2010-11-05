import tkFileDialog
from DChartsSCXMLGenerator import generate
from scxml.cgf.SCXMLCompiler import compile


def exportSCXML(self):
	#launch dialog, choose location to write file, return that location
	file=tkFileDialog.asksaveasfilename(initialfile="out.scxml", 
	      filetypes=[("SCXML files", "*.scxml")], 
	      initialdir=self.initialDirectoryDict[ 'OpenSaveModel' ])

	generate(self.ASGroot.listNodes,file)
	return file

def exportJavaScript(self):
	#FIXME: this code will prompt for a dialog for exportSCXML. maybe we don't want that behaviour?
	location = exportSCXML(self)

	file=tkFileDialog.asksaveasfilename(initialfile="out.js", 
	      filetypes=[("JavaScript files", "*.js")], 
	      initialdir=self.initialDirectoryDict[ 'OpenSaveModel' ])

	results = compile([location]);
	rfile = open(file,"w");
	for result in results:
		rfile.write(result)
	rfile.close()

def startStopDebugServer(self):
	import DChartsDebugServer
	port_number = 12345
	if DChartsDebugServer.isServerRunning():
		DChartsDebugServer.stopServer()
	else:
		DChartsDebugServer.startServer(self, self.ASGroot, port_number)

def startStopClientServer(self):
	import SimpleHTTPPostProxyServer
	port_number = 8000
	proxy_url = "localhost:12345"
	if SimpleHTTPPostProxyServer.isServerRunning():
		SimpleHTTPPostProxyServer.stopServer()
	else:
		regenerateClientServerCode(self)
		SimpleHTTPPostProxyServer.startServer(port_number, proxy_url)

def regenerateClientServerCode(self):
	generate(self.ASGroot.listNodes,"out.scxml")
	results = compile(["out.scxml"])
	#write results
	rfile = open("out.js","w");
	for result in results:
		rfile.write(result)
	rfile.close()
