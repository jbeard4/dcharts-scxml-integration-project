#the thinnest python module to do the following: 
#make it easier to access the accompanying transform (using pkg_resources)
#encapsulate the functionality of this transform
#provide a smaller API than doing the whole thing with lxml (too verbose to put straight into the buttons model)

import sys
import pkg_resources
from lxml import etree

def addPauseSupportToSCXMLDocument(pathToSCXML,outputFile="out.scxml"):
	#get the source document
	sourceDocument =  etree.parse(pathToSCXML)
	
	#do the transform
	transformDocument =  etree.parse(pkg_resources.resource_stream(__name__,"addPauseSupport.xsl"))
	compiledTemplate = etree.XSLT(transformDocument)
	outputDocument = compiledTemplate(sourceDocument) 

	outputDocument.write(outputFile,pretty_print=True)

	return results
