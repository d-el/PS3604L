#!/usr/bin/env python3
# ./pulse.py -i 192.168.0.10

from ps3604l import Ps3604l
import argparse
import time
import datetime

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ipaddr", required=True, help="Device IP address")
args = ap.parse_args()

ps = Ps3604l(args.ipaddr)
ps.target_voltage = 1.8 # V
ps.target_current = 0.05 # A
ps.target_time = 1 # s
ps.target_mode = ps.Mode.timeShutdown
ps.target_enable = 1

while True:
	try:
		ps.target_enable = 1
		print(datetime.datetime.now())
		time.sleep(2)
	except KeyboardInterrupt:
		ps.target_enable = 0
		break
