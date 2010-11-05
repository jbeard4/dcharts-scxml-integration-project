import tkFileDialog
import os
from DChartsSCXMLGenerator import generate
from scxml.cgf.SCXMLCompiler import compile
import DChartsDebugServer
import SimpleHTTPPostProxyServer
import webbrowser

#configuration
dchartsDebugServerPortNumber = 12345
dchartsClientServerPortNumber = 8000

defaultSCXMLOutputFileName = "out.scxml"
defaultJsOutputFileName = "out.js"

def exportSCXML(self):
	#launch dialog, choose location to write file, return that location
	file=tkFileDialog.asksaveasfilename(initialfile=defaultSCXMLOutputFileName, 
	      filetypes=[("SCXML files", "*.scxml")], 
	      initialdir=self.initialDirectoryDict[ 'OpenSaveModel' ])

	self.initialDirectoryDict[ 'OpenSaveModel' ] = os.path.dirname(file) 	#set directory preference

	generate(self.ASGroot.listNodes,file)
	return file

def exportJavaScript(self):
	#FIXME: this code will prompt for a dialog for exportSCXML. maybe we don't want that behaviour?
	location = exportSCXML(self)

	file=tkFileDialog.asksaveasfilename(initialfile=defaultJsOutputFileName, 
	      filetypes=[("JavaScript files", "*.js")], 
	      initialdir=self.initialDirectoryDict[ 'OpenSaveModel' ])

	self.initialDirectoryDict[ 'OpenSaveModel' ] = os.path.dirname(file)	#set directory preference

	results = compile([location]);
	rfile = open(file,"w");
	for result in results:
		rfile.write(result)
	rfile.close()

def startStopDebugServer(self):
	if DChartsDebugServer.isServerRunning():
		DChartsDebugServer.stopServer()
	else:
		DChartsDebugServer.startServer(self, self.ASGroot, dchartsDebugServerPortNumber)

def startStopClientServer(self):
	proxy_url = "localhost:" + str(dchartsDebugServerPortNumber)

	if DChartsHTTPProxyServer.isServerRunning():
		DChartsHTTPProxyServer.stopServer()
	else:
		regenerateClientServerCode(self)
		#TODO: construct query string and open web browser
		DChartsHTTPProxyServer.startServer(dchartsClientServerPortNumber, proxy_url)

		#TODO: use python cgi package here instead, so that things get properly urlencoded
		#FIXME: client.html is hardcoded here, which break modularity
		#FIXME: StatechartExecutionContext is hardcoded here, which at the moment is safe, but breaks modularity
		urlToOpen = "http://localhost:%s/client.html?listenerServerURL=%s&constructorFunctionName=%s&compiledScriptLocation=%s&supportScriptLocation=%s" % (
			proxy_url,
			"StatechartExecutionContext",
			defaultJsOutputFileName,
			"" )

		print "Opening URL %s" % urlToOpen 

		#open web browser window
		webbrowser.open_new(urlToOpen)

def regenerateClientServerCode(self):
	generate(self.ASGroot.listNodes,defaultSCXMLOutputFileName)
	results = compile([defaultSCXMLOutputFileName])
	#write results
	rfile = open(defaultJsOutputFileName,"w");
	for result in results:
		rfile.write(result)
	rfile.close()
