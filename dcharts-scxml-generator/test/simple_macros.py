import re

r = re.compile(r'(?:\[EVENT\("(?P<event>[^"]*)"\s*(,\s*(?P<eventParam>.*))?\)\])|(?:\[DUMP\((?P<dump>.*)\)\])')

m = r.match('[EVENT("resume")]')
print m
print m.group("event")
print m.group("eventParam")

m = r.match('[EVENT("foo",("some data"))]')
print m
print m.group("event")
print m.group("eventParam")
