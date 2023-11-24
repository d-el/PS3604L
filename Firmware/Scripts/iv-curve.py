#!/usr/bin/env python3
# Measure Current–voltage characteristic
# ./iv-curve -i 192.168.1.10 -n 1n4148

from pymodbus.client.sync import ModbusTcpClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.compat import iteritems
from collections import OrderedDict
import argparse
import time
import csv
import os
import subprocess

Rw = 0.022 # [Ohm] Wires resistance
Vlimit = 6 # [V]
Istart = 10 # [mA]
Iend = 500 # [mA]

Ithreshold = 150 # [mA]

Istep1 = 5 # [mA]
Time1 = 500 # [ms]

Istep2 = 20 # [ma]
Time2 = 300 # [ms]

# SetUp
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ipaddr", required=False, help="IP address PS3604L", default="192.168.1.10")
ap.add_argument("-n", "--name", required=True, help="Name")
ap.add_argument("-d", "--description", required=False, help="Description")
args = vars(ap.parse_args())

print("connection to {}".format(args['ipaddr']))
client = ModbusTcpClient(args['ipaddr'])

r = client.read_holding_registers(0, 3, unit=1)
print("Regulator version {major}.{minor}.{patch}".format(major=r.registers[0], minor=r.registers[1], patch=r.registers[2]))

builder = BinaryPayloadBuilder(byteorder=Endian.Big, wordorder=Endian.Little)
builder.add_32bit_uint(Vlimit * 1000000) # V
builder.add_32bit_uint(Istart * 1000) # I
builder.add_16bit_uint(0) # Vdac
builder.add_16bit_uint(0) # Idac
builder.add_16bit_uint(1) # mode: limitation
builder.add_32bit_uint(0) # time
builder.add_16bit_uint(1) # Enable
payload = builder.build()
client.write_registers(0x0100, payload, skip_encode=True, unit=1) # Target
time.sleep(1)

# Create CSV
f = open("{}.csv".format(args['name']), 'w')
writer = csv.writer(f, delimiter = ",")
writer.writerow(['Voltage', 'Current']) # Write heater

# Measure loop
current = Istart
while current < Iend:
	builder2 = BinaryPayloadBuilder(byteorder=Endian.Big, wordorder=Endian.Little)
	builder2.add_32bit_uint(Vlimit * 1000000) # V
	builder2.add_32bit_uint(current * 1000) # I
	payload2 = builder2.to_registers() 
	payload2 = builder2.build()
	client.write_registers(0x0100, payload2, skip_encode=True, unit=1) # Target
	
	if current < Ithreshold:
		current = current + Istep1
		time.sleep(Time1 / 1000)
	else:
		current = current + Istep2
		time.sleep(Time2 / 1000)
	
	result = client.read_holding_registers(0x0200, 8,  unit=1)
	decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Little)
	decoded = OrderedDict([
		        ('Voltage', decoder.decode_32bit_uint()),
		        ('Current', decoder.decode_32bit_uint()),
		        ('Power', decoder.decode_32bit_uint()),
		        ('Resistance', decoder.decode_32bit_uint()),

		    ])
	im = decoded['Current'] / 1000000.0
	um = decoded['Voltage'] / 1000000.0 #- im * Rw
	print("{u}V\t{im}A, (set {i}A)".format(u=um, im=im, i=current/1000.0))
	um = um
	writer.writerow([um, im])

f.close()

# Set 0A, 0V, disable
builder.reset();
builder.add_32bit_uint(0 * 1000000) # V
builder.add_32bit_uint(0 * 1000000) # I
builder.add_16bit_uint(0) # Vdac
builder.add_16bit_uint(0) # Idac
builder.add_16bit_uint(1) # mode: limitation
builder.add_32bit_uint(0) # time
builder.add_16bit_uint(0) # Enable
payload = builder.build()
client.write_registers(0x0100, payload, skip_encode=True, unit=1) # Target

client.close()

# Create Graph
proc = subprocess.Popen(['gnuplot','--persist'], 
                shell=False,
                stdin=subprocess.PIPE,
                )

proc.stdin.write(b"set grid\n")
proc.stdin.write(b"set xtics 0.1\n")
proc.stdin.write(b"set ytics 0.1\n")
proc.stdin.write(b"set xlabel \"Potential (V)\"\n")
proc.stdin.write(b"set ylabel \"Current (A)\"\n")
proc.stdin.write(b"set datafile separator ','\n")
proc.stdin.write(str.encode("plot \"{file}.csv\" skip 1 with lines title \"{title}\"\n".format(file=args['name'], title=args['name'])))
proc.stdin.write(b"pause -1\n")
proc.stdin.close()

#input("Press Enter to continue...")

