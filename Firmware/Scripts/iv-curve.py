#!/usr/bin/env python3
# Measure Current–Voltage characteristic
# Version: 0.2

from ps3604l import Ps3604l
import argparse
import time
import csv
import subprocess
import textwrap

# Settings
Rw = 0.079 # [Ohm] Wires resistance
Vlimit = 5.0 # [V]
Istart = 0.001 # [A]
Iend = 0.1 # [A]

Ithreshold = 0.05 # [A]

Istep1 = 0.001 # [A]
Time1 = 0.4 # [s]

Istep2 = 0.1 # [A]
Time2 = 0.3 # [s]

# SetUp
ap = argparse.ArgumentParser(description='I-V measure',
                            formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=textwrap.dedent('''\
                            Example:
                                ./iv-curve.py -i 192.168.88.11 --name C3D02065E
                            '''))

ap.add_argument("-i", "--ipaddr", required=True, help="IP address PS3604L")
ap.add_argument("-n", "--name", required=True, help="Name")
ap.add_argument("-d", "--description", required=False, help="Description")
args = ap.parse_args()

ps = Ps3604l(args.ipaddr)
ps.regulator.target_voltage = Vlimit
ps.regulator.target_wire_resistance = Rw
print(f'set wire resistance {ps.regulator.target_wire_resistance}Ohm')
ps.regulator.target_current = Istart
ps.regulator.target_mode = ps.regulator.Mode.limitation
ps.regulator.target_time = 0
ps.regulator.target_enable = 1
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
			ps.regulator.target_current = current
			print(f'set {current:5.3f}A, ', end='')
			if current < Ithreshold:
				current = current + Istep1
				time.sleep(Time1)
			else:
				current = current + Istep2
				time.sleep(Time2)
			
			um = ps.regulator.state_voltage
			im = ps.regulator.state_current
			print(f'{um:6.3f}V\t{im:5.3f}A')
			um = um
			writer.writerow([um, im])

		f.close()

		# Set 0A, 0V, disable
		ps.regulator.target_enable = 0
		ps.regulator.target_voltage = 0
		ps.regulator.target_current = 0

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
		ps.regulator.target_enable = 0
		ps.regulator.target_voltage = 0
		ps.regulator.target_current = 0
		break

