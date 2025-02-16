#!/usr/bin/env python3
# Read and write calibration
# version 0.1

from ps3604l import Ps3604l
import argparse
import time
import datetime

ap = argparse.ArgumentParser(description='Calibration dump')
ap.add_argument("-i", "--ipaddr", required=True, help="Device IP address")
ap.add_argument("-w", "--wfilename", required=False, help="File to write dump")
ap.add_argument("-r", "--rfilename", required=False, help="File save dump")
ap.add_argument('-s', '--sn', type=int, help='write serial number')
args = ap.parse_args()

ps = Ps3604l(args.ipaddr)

calibrations = [
	['calibration_time'	,""			,'uint32_t'	,0x0300],
	['dac_max_val'	    ,""			,'uint32_t'	,0x0302],

	['v0_u'				,"V"		    ,'int32_t'	,0x0310],
	['v1_u'				,"V"		    ,'int32_t'	,0x0312],
	['v2_u'				,"V"	    	    ,'int32_t'	,0x0314],
	['v3_u'				,"V"	        	,'int32_t'	,0x0316],
	['v4_u'				,"V"		    ,'int32_t'	,0x0318],
	['v5_u'				,"V"		    ,'int32_t'	,0x031A],
	
	['i0_i'				,"A"		    ,'int32_t'	,0x0320],
	['i1_i'				,"A"		    ,'int32_t'	,0x0322],
	['i2_i'				,"A"		    ,'int32_t'	,0x0324],
	['i3_i'				,"A"		    ,'int32_t'	,0x0326],
	['i4_i'				,"A"		    ,'int32_t'	,0x0328],
	['i5_i'				,"A"		    ,'int32_t'	,0x032A],
	
	['micro_i0_i'		,"A"		    ,'int32_t'	,0x0330],
	['micro_i1_i'		,"A"		    ,'int32_t'	,0x0332],
	['micro_i2_i'		,"A"		    ,'int32_t'	,0x0334],
	
	['v0_adc'			,"lsb"		,'int32_t'	,0x0340],
	['v1_adc'			,"lsb"		,'int32_t'	,0x0341],
	['v2_adc'			,"lsb"		,'int32_t'	,0x0342],
	['v3_adc'			,"lsb"		,'int32_t'	,0x0343],
	['v4_adc'			,"lsb"		,'int32_t'	,0x0344],
	['v5_adc'			,"lsb"		,'int32_t'	,0x0345],
	
	['v0_dac'			,"lsb"		,'int32_t'	,0x0350],
	['v1_dac'			,"lsb"		,'int32_t'	,0x0351],
	['v2_dac'			,"lsb"		,'int32_t'	,0x0352],
	['v3_dac'			,"lsb"		,'int32_t'	,0x0353],
	['v4_dac'			,"lsb"		,'int32_t'	,0x0354],
	['v5_dac'			,"lsb"		,'int32_t'	,0x0355],
	
	['i0_adc'			,"lsb"		,'uint32_t'	,0x0360],
	['i1_adc'			,"lsb"		,'int32_t'	,0x0361],
	['i2_adc'			,"lsb"		,'int32_t'	,0x0362],
	['i3_adc'			,"lsb"		,'int32_t'	,0x0363],
	['i4_adc'			,"lsb"		,'int32_t'	,0x0364],
	['i5_adc'			,"lsb"		,'int32_t'	,0x0365],
	
	['i0_dac'			,"lsb"		,'int32_t'	,0x0370],
	['i1_dac'			,"lsb"		,'int32_t'	,0x0371],
	['i2_dac'			,"lsb"		,'int32_t'	,0x0372],
	['i3_dac'			,"lsb"		,'int32_t'	,0x0373],
	['i4_dac'			,"lsb"		,'int32_t'	,0x0374],
	['i5_dac'			,"lsb"		,'int32_t'	,0x0375],
	
	['iext0_adc'		    ,"lsb"		,'int32_t'	,0x0380],
	['iext1_adc'		    ,"lsb"		,'int32_t'	,0x0382],
	['iext2_adc'		    ,"lsb"		,'int32_t'	,0x0384],
	['iext3_adc'		    ,"lsb"		,'int32_t'	,0x0386],
	['iext4_adc'		    ,"lsb"		,'int32_t'	,0x0388],
	['iext5_adc'		    ,"lsb"		,'int32_t'	,0x038A],
	
	['micro_iext0_adc'	,"lsb"		,'int32_t'	,0x0390],
	['micro_iext1_adc'	,"lsb"		,'int32_t'	,0x0392],
	['micro_iext2_adc'	,"lsb"		,'int32_t'	,0x0394]
]

if args.sn:
	print('write serial number: {}'.format(args.sn))
	ps._Ps3604l__write_u32(0x0004, args.sn)

if args.rfilename or (args.rfilename == None and args.wfilename == None):
	file = None
	if args.rfilename:
		file = open(args.rfilename, 'w')
	for parameter in calibrations:
		val=None
		pname = parameter[0]
		ptype = parameter[2]
		paddr = parameter[3]
		if ptype == 'uint32_t':
			val = ps._Ps3604l__read_u32(paddr)
		if ptype == 'int32_t':
			val = ps._Ps3604l__read_i32(paddr)
		if ptype == 'uint16_t':
			val = ps._Ps3604l__read_u16(paddr)
		print('read {} {} [{}] {}'.format(pname, ptype, hex(paddr), val))
		s = pname + ',' + ptype + ',' + hex(paddr) + ',' + str(val)
		if file:
			file.write(s + '\n')
	if file:
		file.close()

if args.wfilename:
	file = open(args.wfilename, 'r')
	print('Do you want write calibration data to device? [y/n]')
	resp = input()
	if resp != 'y' and resp != 'Y':
		print('Exit')
		quit()
	lines = file.readlines()
	for l in lines:
		parameter = [x.strip() for x in l.split(',')]
		pname = parameter[0]
		ptype = parameter[1]
		paddr = int(parameter[2], 16)
		pval = int(parameter[3])
		print('write {} {} [{}] {}'.format(pname, ptype, paddr, pval))
		if ptype == 'uint32_t':
			val = ps._Ps3604l__write_u32(paddr, pval)
		if ptype == 'int32_t':
			val = ps._Ps3604l__write_i32(paddr, pval)
		if ptype == 'uint16_t':
			val = ps._Ps3604l__write_u16(paddr, pval)
	ps.target_save_settings = 1
	print('Write done')


