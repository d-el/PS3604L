#!/usr/bin/python3
# Version: 0.1

import vxi11
import sys

adapter = vxi11.list_devices()[0]
print(f'Finded adapter: {adapter}')

l=[]
f=[]
d = vxi11.InterfaceDevice(adapter,'gpib0')

for n in range(1, 30):
	try:
		inst = vxi11.Instrument(adapter,'gpib0,{0}'.format(n))
		inst.timeout = 1
		inst.open()
		inst.lock()
		f = d.find_listeners([n]) # if I do the whole range at once it will interfere...
		if f != []:
			idn = inst.ask("*IDN?")
			if idn == '?':
			    idn = inst.ask("IDN?")
			print(f'[{n:02}]: {idn}')
			l.append(f[0])
		inst.unlock()
		inst.close()
		del inst
	except:
		e=sys.exc_info()[0]
		#print("Error on inst no.: {0}\n{1}".format(n,e))
		del inst

print("Done")

