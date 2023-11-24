#!/usr/bin/env python3

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

# SetUp
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ipaddr", required=False, help="IP address PS3604L", default="192.168.1.10")
args = vars(ap.parse_args())

print("connection to {}".format(args['ipaddr']))
client = ModbusTcpClient(args['ipaddr'])

r = client.read_holding_registers(0, 3, unit=1)
print("Regulator version {major}.{minor}.{patch}".format(major=r.registers[0], minor=r.registers[1], patch=r.registers[2]))

# Measure loop
i = 0
while i < 1:
	#result = client.read_holding_registers(0x0500, 8,  unit=1)
	#decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Little)
	#decoded = OrderedDict([
	#	        ('v0_u', decoder.decode_32bit_uint()),
	#	        ('v1_u', decoder.decode_32bit_uint()),
	#	        ('v2_u', decoder.decode_32bit_uint()),
	#	        ('v3_u', decoder.decode_32bit_uint()),
	#	    ])
	#print(decoded)
	
	result = client.read_holding_registers(0x0600, 8,  unit=1)
	decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Little)
	decoded = OrderedDict([
	        ('i0_i', decoder.decode_32bit_uint()),
	        ('i1_i', decoder.decode_32bit_uint()),
	        ('v2_i', decoder.decode_32bit_uint()),
	        ('v3_i', decoder.decode_32bit_uint()),
	    ])
	print(decoded)
	
	result = client.read_holding_registers(0x0700, 8,  unit=1)
	decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Little)
	decoded = OrderedDict([
	        ('iext0_i', decoder.decode_32bit_uint()),
	        ('iext1_i', decoder.decode_32bit_uint()),
	        ('iext2_i', decoder.decode_32bit_uint()),
	        ('iext3_i', decoder.decode_32bit_uint()),
	    ])
	print(decoded)
	
	result = client.read_holding_registers(0x0810, 8,  unit=1)
	decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Little)
	decoded = OrderedDict([
	        ('iext0_adc', decoder.decode_32bit_int()),
	        ('iext1_adc', decoder.decode_32bit_int()),
	        ('iext2_adc', decoder.decode_32bit_int()),
	        ('iext3_adc', decoder.decode_32bit_int()),
	    ])
	print(decoded)
	
	print("\n")
	time.sleep(1)

