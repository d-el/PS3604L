#!/usr/bin/env python3
# Accuracy measure
# version 0.1

from ps3604l import Ps3604l
import argparse
import time
import csv
import serial
from pymeasure.adapters import SerialAdapter
from pymeasure.instruments.hp import HP34401A
import subprocess


Vmin = 0
Vth = 0
Vmax = 0
Vstep1 = 0
Vstep2 = 0
Time1 = 0
Time2 = 0

# SetUp
ap = argparse.ArgumentParser(description='accuracy_test')
ap.add_argument("-i", "--ipaddr", required=False, help="IP address PS3604L", default="192.168.88.11")
ap.add_argument("-n", "--name", required=True, help="Name")
ap.add_argument("-s", "--serial", help="Serial port name")
ap.add_argument('-c', "--current", help='Meas Voltage', action='store_true')
ap.add_argument('-p', "--plot", help='Plot only', action='store_true')
args = ap.parse_args()

if args.current:
	Vinit_v = 10	# [V]
	Vinit_c = 0		# [A]
	Vmin = 0.001	# [A]
	Vth = 0.010		# [A]
	Vmax = 4.0		# [A]
	Vstep1 = 0.001	# [A]
	Vstep2 = 0.1	# [A]
	Time1 = 1		# [s]
	Time2 = 1		# [s]
	unit = 'A'
	dmm_function = 'DCI'
else:
	Vinit_v = 0		# [V]
	Vinit_c = 1		# [A]
	Vmin = 0.01		# [V]
	Vth = 0.5		# [V]
	Vmax = 36		# [V]
	Vstep1 = 0.1	# [V]
	Vstep2 = 1		# [V]
	Time1 = 1		# [s]
	Time2 = 1		# [s]
	unit = 'V'
	dmm_function = 'DCV'

if not args.plot:
	# Open power supply
	ps = Ps3604l(args.ipaddr)
	ps.target_voltage = Vinit_v
	ps.target_current = Vinit_c
	ps.target_mode = ps.Mode.limitation
	ps.target_time = 0
	ps.target_enable = 1
	time.sleep(0.1)

	# Open DMM
	adapter = SerialAdapter(port=args.serial,
		                    baudrate = 9600, # Recommend value
		                    parity = serial.PARITY_NONE,
		                    stopbits = serial.STOPBITS_TWO,
		                    bytesize = serial.EIGHTBITS,
		                    xonxoff=False,
		                    dsrdtr=True,
		                    rtscts=False,
		                    write_termination="\n",
		                    read_termination="\n",
		                    )
	dmm = HP34401A(adapter)
	dmm.reset() # wait for reset
	time.sleep(1)
	dmm.clear()
	dmm.write('SYSTem:REMote')
	dmm.status # for lush input buffers
	print('dmm: {}, SCPI: {}, terminals: {}'.format(dmm.id, dmm.scpi_version, dmm.terminals_used))
	dmm.function_ = dmm_function

	# Create CSV
	f = open("{}.csv".format(args.name), 'w')
	writer = csv.writer(f, delimiter = ",")
	writer.writerow(['set', 'set error', 'readback error']) # Write heater

	time.sleep(2)
	try:
		# Measure loop
		vset = Vmin
		vstep = 0
		while vset <= Vmax:
			if args.current:
				ps.target_current = vset
			else:
				ps.target_voltage = vset
			
			if vset < Vth:
				vstep = Vstep1
				time.sleep(Time1)
			else:
				vstep = Vstep2
				time.sleep(Time2)

			vmeas = ps.state_current if args.current else ps.state_voltage
			vdmm = dmm.reading
			wr_error = vmeas - vset
			vset_error = vset - vdmm
			print(f'set {vset:2.3f}{unit}, meas {vmeas:2.3f}{unit}, vdmm {vdmm:2.4f}{unit}, set_error {vset_error:2.4f}{unit}, wr_error {wr_error:2.4f}{unit}')
			
			writer.writerow([vset, vset_error, wr_error])
			
			if vset == Vmax:
				break
			vset = vset + vstep
			if vset > Vmax:
				vset = Vmax
		
		ps.target_voltage = 0
		ps.target_current = 0
		ps.target_enable = 0
		f.close()
		
	except KeyboardInterrupt:
		ps.target_enable = 0
		ps.target_voltage = 0
		ps.target_current = 0
		exit(0)
	
# Create Graph
proc = subprocess.Popen(['gnuplot','--persist'], 
		        shell=False,
		        stdin=subprocess.PIPE,
		        )
proc.stdin.write(b"set grid\n")
proc.stdin.write(b"set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor rgb\"#3D3846\" behind\n")
proc.stdin.write(b"set datafile separator ','\n")
proc.stdin.write(b"set key autotitle columnhead\n")
proc.stdin.write(str.encode(f"set xlabel \"Set ({unit})\"\n"))
proc.stdin.write(str.encode(f"set ylabel \"Error ({unit})\"\n"))
proc.stdin.write(str.encode(f"set title \"{args.name}\"\n"))
proc.stdin.write(str.encode(f"plot \"{args.name}.csv\" using 1:2 with lines, '' using 1:3 with lines\n"))
proc.stdin.write(b"pause -1\n")
proc.stdin.close()

