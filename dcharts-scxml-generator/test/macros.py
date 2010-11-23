import re

#AFTER(1)
#in action or guard code:
eventRE = re.compile(r'(?:\[EVENT\("(?P<event>[^"]*)"\)\])|(?:\[INSTATE\("(?P<instate>[^"]*)"\)\])|(?:\[DUMP\((?P<dump>.*)\)\])')
paramsRE = re.compile(r"\[PARAMS\]")
#the only one that should go in guard is INSTATE

testEvent = '[EVENT("alarmStart")]'
testEvent2 = '''controller.stopSelection()
[EVENT("resume")] aldskjfaslk
[INSTATE("NORMAL_MODE.MODE.RUN_CHR")] [EVENT("foo")]
[DUMP("Starting the Digital Watch")]
[DUMP([PARAMS[0]])]
moar text
			[PARAMS]
	woasijarar
'''

#testInstate = '[INSTATE("NORMAL_MODE.MODE.RUN_CHR")]'
#testDump = ''
#testParams = '[PARAMS]'

#print(eventRE.match(testEvent))
#print(eventRE.match(testInstate))
iter = eventRE.finditer(testEvent2)

"""
for match in iter:
	print match.span()
	print match.group()
	print match.group("event")
	print match.group("instate")
	print "---------------"
"""

prevend = 0
for match in iter:
	script = testEvent2[prevend:match.span()[0]].strip()
	if script:
		print "<script>" + script + "</script>"

	prevend = match.span()[1]

	#should only be one for each iteration
	event = match.group("event")
	state = match.group("instate")
	dump = match.group("dump")
	#params = match.group("params")

	if event:
		print '<send event="%s"/>' % event
	elif state:
		print 'In(%s)' % state
	elif dump:
		print '<log>%s</log>' % dump
	#elif params:
	#	print '_event.data'
	else:
		pass

script = testEvent2[prevend:].strip()
if script:
	print "<script>" + script + "</script>"
