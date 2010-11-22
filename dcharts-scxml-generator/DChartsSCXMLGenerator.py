#lxml import dance
try:
	from lxml import etree
	print("running with lxml.etree")
except ImportError:
	try:
		# Python 2.5
		import xml.etree.cElementTree as etree
		print("running with cElementTree on Python 2.5+")
	except ImportError:
		try:
			# Python 2.5
			import xml.etree.ElementTree as etree
			print("running with ElementTree on Python 2.5+")
		except ImportError:
			try:
				# normal cElementTree install
				import cElementTree as etree
				print("running with cElementTree")
			except ImportError:
				try:
					# normal ElementTree install
					import elementtree.ElementTree as etree
					print("running with ElementTree")
				except ImportError:
					print("Failed to import ElementTree from any known place")

import re
import pdb

#{'Hyperedge': [<Hyperedge.Hyperedge instance at 0xb73ef6c>], 'Orthogonal': [], 'Composite': [<Composite.Composite instance at 0xb63660c>], 'ASG_DCharts': [], 'contains': [<contains.contains instance at 0xb735d6c>], 'ASG_DChartsSCXMLGenerator': [], 'Class_0': [], 'orthogonality': [], 'Server': [], 'connection': [], 'visual_settings': [], 'Basic': [<Basic.Basic instance at 0xb735d8c>, <Basic.Basic instance at 0xb735dac>], 'Port': [], 'History': []}

scxmlNS = "{http://www.w3.org/2005/07/scxml}";

# these regular expressions are for finding DCharts macros
actionCodeRE = re.compile(r'(?:\[EVENT\("(?P<event>[^"]*)"\)\])|(?:\[DUMP\("(?P<dump>[^"]*)"\)\])')
paramsRE = re.compile(r"\[PARAMS\]")
instateRE = re.compile(r'\[INSTATE\("(?:[^.]*\.)*([^"]*)"\)\]')
afterRE = re.compile(r'AFTER\(([^)]*)\)')


def dchartsActionCodeToSCXML(parentElement,code):
	iter = actionCodeRE.finditer(code) 
	
	#print(code)
	#pdb.set_trace()
	
	#first pass
	scripts = []
	prevend = 0
	for match in iter:
		scriptText = code[prevend:match.span()[0]].strip()

		if scriptText:
			script = etree.SubElement(parentElement,scxmlNS + "script")
			script.text = scriptText 

			scripts.append(script)

		#should only be one for each iteration
		event = match.group("event")
		dump = match.group("dump")

		if event:
			etree.SubElement(parentElement,scxmlNS + "send",{"event":event})
		elif dump:
			log = etree.SubElement(parentElement,scxmlNS + "log")
			log.text = dump
		else:
			pass

		prevend = match.span()[1]

	scriptText = code[prevend:].strip()
	if scriptText:
		script = etree.SubElement(parentElement,scxmlNS + "script")
		script.text = scriptText 

		scripts.append(script)

	#second pass, replace [PARAM] and [INSTATE]
	for script in scripts:
		script.text = paramsRE.sub("_event.data",script.text)
		script.text = instateRE.sub(r"In(\1)",script.text)


def generate(nodeListDict,outFilePath="out.scxml"):
	#set up all the inner functions and variables we need
	#we use inner functions here so that we don't need to pass around a reference to doc

	scxmlRoot = etree.Element(scxmlNS + "scxml",{"version":"1.0","profile":"ecmascript"})

	elementIds = set() #we need this later on because etree doesn't have getelementbyid

	historyCounter = 0;

	#some helper functions

	def getId(anything):
		return anything.name.toString().strip() or (anything.getClass()=="History" and "$history_%d" % historyCounter)

	def setupTopLevelState(state,e):
		#check if he's top-level 
		if not [conn for conn in state.in_connections_ if conn in nodeListDict['contains'] or conn in nodeListDict['orthogonality']]:

			#go ahead and append him to the root
			scxmlRoot.append(e)

			# set initial state on the scxml root
			if state.is_default.getValueBoolean():
				initial = etree.SubElement(scxmlRoot,scxmlNS + "initial")
				etree.SubElement(initial,scxmlNS + "transition",{"target":e.attrib["id"]})


	def getDefaultStateFromParent(parentState):
		defaultChild = filter( lambda child : child.is_default.getValueBoolean(),
			reduce(lambda linkList1, linkList2: linkList1 + linkList2,
				map(lambda link : link.out_connections_, 
					filter(lambda link : link in nodeListDict['contains'], parentState.out_connections_)),[]))

		if len(defaultChild):
			return defaultChild[0]
		else:
			return None

	#some conversion functions

	def hyperedgeToSCXML(hyperedge):
		e = etree.Element(scxmlNS+"transition")

		targetNames = map(getId, hyperedge.out_connections_)
		targetNamesString = " ".join(targetNames)

		e.attrib["target"]=targetNamesString

		trigger = hyperedge.trigger.toString().strip()
		if trigger:
			e.attrib["event"]=trigger

		guard = hyperedge.guard.toString().strip()
		if guard and not guard is "1":
			e.attrib["cond"]=instateRE.sub(r"In(\1)",guard)

		scriptText = hyperedge.action.toString().strip()
		if scriptText:
			dchartsActionCodeToSCXML(e,scriptText)
			
		return e

	def orthogonalToSCXML(orthogonal):
		id = getId(orthogonal)

		e = etree.Element(scxmlNS + "state",{"id":id})

		elementIds.add(id) #add him to elementIds set

		#set up initial state
		defaultChildState = getDefaultStateFromParent(orthogonal)

		if defaultChildState :
			initial = etree.SubElement(e,scxmlNS + "initial")
			transition = etree.SubElement(initial,scxmlNS + "transition",{"target":getId(defaultChildState)})

		return e

	def compositeToSCXML(composite):

		e = None
		id = getId(composite)
		#he is either a state or a parallel
		#we say here that if he has an orthogonality relationship, he's a parallel
		if filter(lambda link : link in nodeListDict['orthogonality'], composite.out_connections_):
			e = etree.Element(scxmlNS + "parallel",{"id":id})
		else:
			e = etree.Element(scxmlNS + "state",{"id":id})

		elementIds.add(id) #add him to elementIds set

		enterActionText = composite.enter_action.toString().strip()
		if enterActionText:
			onentry = etree.SubElement(e,scxmlNS + "onentry")
			dchartsActionCodeToSCXML(onentry,enterActionText)

		exitActionText = composite.exit_action.toString().strip()
		if exitActionText:
			onexit = etree.SubElement(e,scxmlNS + "onexit")
			dchartsActionCodeToSCXML(onexit,exitActionText)

		#set up initial state
		defaultChildState = getDefaultStateFromParent(composite)

		if defaultChildState :
			initial = etree.SubElement(e,scxmlNS + "initial")
			transition = etree.SubElement(initial,scxmlNS + "transition",{"target":getId(defaultChildState)})

		setupTopLevelState(composite,e)
		
		#print(etree.tostring(e, pretty_print=True))
		return e

	basicToSCXML = compositeToSCXML

	def historyToSCXML(history):
		print("HEREHEREHEREHEREHEREHEREHERE")
		type = None
		id = getId(history)
		if history.star.getValueBoolean():
			type = "deep"
		else:
			type = "shallow"
		e = etree.Element(scxmlNS + "history",{"id":id,"type":type})

		elementIds.add(id) #add him to elementIds set

		setupTopLevelState(history,e)

		return e

	dchartsToSCXMLMap = {
		'Hyperedge': hyperedgeToSCXML, 
		'Orthogonal': orthogonalToSCXML, 
		'Composite': compositeToSCXML, 
		'Basic': basicToSCXML, 
		'History': historyToSCXML
	}

	instanceMap = {} #maps atom3 objects to xml nodes

	#map everything to its XML representation
	for k,v in nodeListDict.items():
		if k in dchartsToSCXMLMap.keys():
			for atom3object in v:
				instanceMap[atom3object] = dchartsToSCXMLMap[k](atom3object) 

	print(instanceMap)
	
	#go through and glue everything together

	#hook up containment relationships
	for k,v in filter(lambda (k,v) : k in ['contains','orthogonality'], nodeListDict.items()) :
		for atom3object in v:
			xmlParent = instanceMap[atom3object.in_connections_[0]];
			xmlChildren = map(lambda o : instanceMap[o],atom3object.out_connections_)
			for child in xmlChildren:
				xmlParent.append(child)

	#hook up hyperedges
	for hyperedge in nodeListDict['Hyperedge']:
		xmlParent = instanceMap[hyperedge.in_connections_[0]];
		xmlTransition = instanceMap[hyperedge];

		xmlParent.append(xmlTransition )

	#transform dcharts AFTER events
	specialTimeoutEventNameCounter = -1
	specialTimeoutEventNameBase = "$timeout_"
	sendIdCounter = 0
	sendIdBase = "$send_"
	for hyperedge in nodeListDict['Hyperedge']:
		m = afterRE.match(hyperedge.trigger.toString().strip())
		if m:

			xmlParent = instanceMap[hyperedge.in_connections_[0]]
			xmlTransition = instanceMap[hyperedge];

			#create a unique event name
			specialTimeoutEventNameCounter = specialTimeoutEventNameCounter + 1
			uniqueEventName = specialTimeoutEventNameBase + str(specialTimeoutEventNameCounter)
			while filter(lambda h : h.trigger.toString().strip() is uniqueEventName, nodeListDict['Hyperedge']):
				specialTimeoutEventNameCounter = specialTimeoutEventNameCounter + 1
				uniqueEventName = specialTimeoutEventNameBase + str(specialTimeoutEventNameCounter)

			
			#update xml transition with new event name
			xmlTransition.attrib["event"] = uniqueEventName 
			
			#instrument action code on onentry and onexit

			#if needed, create onentry and onexit
			onentry = xmlParent.find(scxmlNS + "onentry")
			if not onentry:
				#create it
				onentry = etree.SubElement(xmlParent,scxmlNS + "onentry")

			onexit = xmlParent.find(scxmlNS + "onexit")
			if not onexit:
				#create it
				onexit = etree.SubElement(xmlParent,scxmlNS + "onexit")

			#create unique id for send element
			sendId = sendIdBase + str(sendIdCounter)
			while sendId in elementIds:
				sendIdCounter = sendIdCounter + 1
				sendId = sendIdBase + str(sendIdCounter)
				
			#create and append send and cancel elements
			delay = m.group(1)
			etree.SubElement(onentry,scxmlNS + "send",{"delay":delay,"event":uniqueEventName,"id":sendId})
			elementIds.add(sendId)	#add him to elementIds
			
			etree.SubElement(onexit,scxmlNS + "cancel",{"sendid":sendId})


	print(etree.tostring(scxmlRoot, pretty_print=True))
	et = etree.ElementTree(scxmlRoot)
	et.write(outFilePath,pretty_print=True)

	return scxmlRoot
