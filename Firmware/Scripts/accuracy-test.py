#!/usr/bin/env python3
# Accuracy measure
# Version: 0.2

from ps3604l import Ps3604l
import argparse
import time
import csv
import vxi11
from pymeasure.adapters import SerialAdapter
from pymeasure.instruments.hp import HP34401A
from pymeasure.instruments.keithley import keithley2001
import pyvisa
import subprocess
import textwrap

class k2001:
    def __init__(self, adapter):
        self.meter = keithley2001.Keithley2001(adapter)
        self.meter.display_enable(True, True)
    
    def setupVoltage(self):
        self.meter.measure_voltage()
        self.meter.voltage_nplc = 10
    def getVoltage(self):
        return self.meter.voltage
    def setupCurrent(self):
        self.meter.measure_current()
        self.meter.current_nplc = 10
    def getCurrent(self):
        return self.meter.current

class h34401:  
    def __init__(self, adapter):
        self.meter = HP34401A(adapter)
        self.meter.clear()
        print(f'dmm: terminals: {self.meter.terminals_used}')
	
    def setupVoltage(self):
        self.meter.function_ = 'DCV'
    def getVoltage(self):
        self.meter.reading
        return (self.meter.reading + self.meter.reading + self.meter.reading) / 3
    def setupCurrent(self):
        self.meter.function_ = 'DCI'
    def getCurrent(self):
        return self.meter.reading

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='accuracy_test',formatter_class=argparse.RawDescriptionHelpFormatter,
                            epilog=textwrap.dedent('''\
                            Example:
                                Measure voltage
                                    ./accuracy-test.py -i 192.168.88.11 -b 23 -d h -n PS3604L-sn2-hp
                                    ./accuracy-test.py -i 192.168.88.11 -b 28 -d k -n PS3604L-sn2-k2001
                                Measure current
                                    ./accuracy-test.py -i 192.168.88.11 -c -b 23 -d h -n PS3604L-sn2-hp
                                    ./accuracy-test.py -i 192.168.88.11 -c -b 28 -d k -n PS3604L-sn2-k2001
                                Plot only
                                    ./accuracy-test.py -n PS3604L-sn2-k2001 -p
                            '''))
    ap.add_argument('-i', '--ipaddr', required=False, help='IP address PS3604L')
    ap.add_argument('-b', '--gpib', help='GPIB adress')
    ap.add_argument('-a', '--adapterip', required=False, help='Adapter IP address')
    ap.add_argument('-d', '--dmm', type=str, required=False, default='h', help='Multimeter: h - HP34401, k - K2001')
    ap.add_argument('-n', '--name', required=True, help='Name')
    ap.add_argument('-c', '--current', help='Meas current', action='store_true')
    ap.add_argument('-p', '--plot', help='Plot only', action='store_true')
    args = ap.parse_args()

    if args.current:
	    config_init_v = 10	    # [V]
	    config_init_c = 0.0001	# [A]
	    config_min = 0.001	    # [A]
	    config_th = 0.010		# [A]
	    config_max = 1.0		    # [A]
	    config_step1 = 0.001	    # [A]
	    config_step2 = 0.1    	# [A]
	    config_time1 = 0.5	    # [s]
	    config_time2 = 0.5	    # [s]
	    config_unit = 'A'
    else:
	    config_init_v = 0		# [V]
	    config_init_c = 1		# [A]
	    config_min = 35		    # [V]
	    config_th = 34.0        # [V]
	    config_max = 36.0       # [V]
	    config_step1 = 0.1     	# [V]
	    config_step2 = 0.1		# [V]
	    config_time1 = 1.6		# [s]
	    config_time2 = 1.6		# [s]
	    config_unit = 'V'

    # Measure
    if not args.plot:
	    # Open power supply
	    ps = Ps3604l(args.ipaddr)
	    ps.regulator.target_voltage = config_init_v
	    ps.regulator.target_current = config_init_c
	    ps.regulator.target_mode = ps.regulator.Mode.limitation
	    ps.regulator.target_time = 0
	    ps.regulator.target_enable = 1
	    time.sleep(2)
	    
	    if args.adapterip:
	        adapter_ip = args.adapterip
	    else:
	        adapter_ip = vxi11.list_devices()[0]
	        print(f'Finded adapter: {adapter_ip}')
	    dmm_adapter = vxi11.Instrument(adapter_ip, f"gpib0,{args.gpib}")

	    # Open DMM
	    if args.dmm == 'h':
	        print('Select HP 34401')
	        dmm = h34401(dmm_adapter)
	    else:
	        print('Select Keithley 2001')
	        dmm = k2001(dmm_adapter)
	    if args.current:
		    dmm.setupCurrent();
	    else:
		    dmm.setupVoltage();

	    # Create CSV
	    f = open("{}.csv".format(args.name), 'w')
	    writer = csv.writer(f, delimiter = ",")
	    writer.writerow(['set', 'set error', 'readback error']) # Write heater

	    time.sleep(2)
	    try:
		    # Measure loop
		    vset = config_min
		    vstep = 0
		    while vset <= config_max:
			    if args.current:
				    ps.regulator.target_current = vset
			    else:
				    ps.regulator.target_voltage = vset
			    if vset < config_th:
				    vstep = config_step1
				    time.sleep(config_time1)
			    else:
				    vstep = config_step2
				    time.sleep(config_time2)

			    vmeas = ps.regulator.state_current if args.current else ps.regulator.state_voltage
			    vdmm = dmm.getVoltage() if args.current else dmm.getCurrent()
			    wr_error = vmeas - vset
			    vset_error = vdmm - vset
			    print('set {:<8.4f}{}, meas {:<8.4f}{}, dmm {:<8.4f}{}, set_error {:<8.4f}{}, wr_error {:<8.4f}{}'.format(
			    vset, config_unit,
			    vmeas, config_unit,
			    vdmm, config_unit,
			    vset_error, config_unit,
			    wr_error, config_unit
			    ))
			    
			    writer.writerow([vset, vset_error, wr_error])
			    
			    if vset == config_max:
				    break
			    vset = vset + vstep
			    if vset > config_max:
				    vset = config_max
		    
		    ps.regulator.target_voltage = 0
		    ps.regulator.target_current = 0.0001
		    ps.regulator.target_enable = 0
		    f.close()
		    
	    except KeyboardInterrupt:
		    ps.regulator.target_enable = 0
		    ps.regulator.target_voltage = 0
		    ps.regulator.target_current = 0.0001
		    exit(0)
	    
    # Plot
    proc = subprocess.Popen(['gnuplot','--persist'], 
		            shell=False,
		            stdin=subprocess.PIPE,
		            )
    proc.stdin.write(b"set grid\n")
    proc.stdin.write(b"set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor rgb\"#3D3846\" behind\n")
    proc.stdin.write(b"set datafile separator ','\n")
    proc.stdin.write(b"set key autotitle columnhead\n")
    proc.stdin.write(str.encode(f"set xlabel \"Set ({config_unit})\"\n"))
    proc.stdin.write(str.encode(f"set ylabel \"Error ({config_unit})\"\n"))
    proc.stdin.write(str.encode(f"set title \"{args.name}\"\n"))
    proc.stdin.write(str.encode(f"plot \"{args.name}.csv\" using 1:2 with lines, '' using 1:3 with lines\n"))
    proc.stdin.write(b"pause -1\n")
    proc.stdin.close()

