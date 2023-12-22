#!/usr/bin/env python3
# Measure Current–voltage characteristic
# ./iv-curve -i 192.168.0.10 -n 1n4148

from ps3604l import Ps3604l
import argparse
import datetime
from collections import OrderedDict
import time
import csv
import os
import subprocess

Rw = 0.022 # [Ohm] Wires resistance
Vlimit = 6 # [V]
Istart = 0.01 # [A]
Iend = 0.4 # [A]

Ithreshold = 0.15 # [A]

Istep1 = 0.005 # [A]
Time1 = 0.5 # [s]

Istep2 = 0.02 # [A]
Time2 = 0.3 # [s]

# SetUp
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ipaddr", required=False, help="IP address PS3604L", default="192.168.1.10")
ap.add_argument("-n", "--name", required=True, help="Name")
ap.add_argument("-d", "--description", required=False, help="Description")
args = ap.parse_args()

ps = Ps3604l(args.ipaddr)
ps.target_voltage = Vlimit
ps.target_current = 0
ps.target_mode = ps.Mode.limitation
ps.target_enable = 1
time.sleep(0.1)

# Create CSV
f = open("{}.csv".format(args.name), 'w')
writer = csv.writer(f, delimiter = ",")
writer.writerow(['Voltage', 'Current']) # Write heater

while True:
	try:
		# Measure loop
		current = Istart
		while current < Iend:
			ps.target_current = current
			
			if current < Ithreshold:
				current = current + Istep1
				time.sleep(Time1)
			else:
				current = current + Istep2
				time.sleep(Time2)
			im = ps.state_voltage
			um = ps.state_current #- im * Rw
			print("{u}V\t{im}A, (set {i}A)".format(u=um, im=im, i=current))
			um = um
			writer.writerow([um, im])

		f.close()

		# Set 0A, 0V, disable
		ps.target_voltage = 0
		ps.target_current = 0
		ps.target_enable = 0

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
		proc.stdin.write(str.encode("plot \"{file}.csv\" skip 1 with lines title \"{title}\"\n".format(file=args.name, title=args.name)))
		proc.stdin.write(b"pause -1\n")
		proc.stdin.close()
		break
		
	except KeyboardInterrupt:
		ps.target_enable = 0
		break

