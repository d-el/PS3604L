#!/usr/bin/env python3
# version 0.1

from ps3604l import Ps3604l
import argparse
import time
import datetime

ap = argparse.ArgumentParser(description='Pulse generator')
ap.add_argument("-i", "--ipaddr", required=True, help="Device IP address")
ap.add_argument("-t", "--time", required=False, type=float, default=0.1)
args = ap.parse_args()

ps = Ps3604l(args.ipaddr)
ps.regulator.target_voltage = 4.0 # V
ps.regulator.target_current = 0.05 # A
ps.regulator.target_time = args.time # s
ps.regulator.target_mode = ps.regulator.Mode.limitation
ps.regulator.target_enable = 1

while True:
	try:
		ps.regulator.target_enable = 1
		print(datetime.datetime.now())
		time.sleep(1)
	except KeyboardInterrupt:
		ps.regulator.target_enable = 0
		ps.regulator.target_voltage = 0
		ps.regulator.target_current = 0
		break
