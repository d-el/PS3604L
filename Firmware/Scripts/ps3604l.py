#!/usr/bin/env python3
# ./ps3604l -i 192.168.0.10

from pymodbus import (
    ExceptionResponse,
    Framer,
    ModbusException,
    pymodbus_apply_logging_config,
    payload,
    constants,
    client
)
import argparse
import time
import datetime
import enum

class Ps3604l():
	slaveaddr = 1

	def __init__(self, ip, port=502):
		self.client = client.ModbusTcpClient(ip, port=port)
		print('connection to {}:{}'.format(ip, port))
		r = self.client.read_holding_registers(0x0000, 3, slave=self.slaveaddr)
		print('Regulator version {major}.{minor}.{patch}'.format(major=r.registers[0], minor=r.registers[1], patch=r.registers[2]))
	
	class Mode(enum.Enum):
		overcurrentShutdown = 0
		limitation = 1
		timeShutdown = 2
		lowCurrentShutdown = 3
		dacMode = 4
	
	class Status(enum.Flag):
		errorExternalIAdc = 1
		errorTemperatureSensor = 2
		overheated = 4
		lowInputVoltage = 8
		reverseVoltage = 16
		notCalibrated = 32
		limitation = 64
		externaIAdc = 128
	
	def __write_u16(self, reg, val):
		self.client.write_register(reg, val)
		
	def __read_u16(self, reg):
		r = self.client.read_holding_registers(reg, 1, slave=self.slaveaddr)
		return r.registers[0]
	
	def __read_i16(self, reg):
		result = self.client.read_holding_registers(reg, 1,  slave=self.slaveaddr)
		decoder = payload.BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=constants.Endian.BIG, wordorder=constants.Endian.LITTLE)
		return decoder.decode_16bit_int()

	def __write_u32(self, reg, val):
		builder = payload.BinaryPayloadBuilder(byteorder=constants.Endian.BIG, wordorder=constants.Endian.LITTLE)
		builder.add_32bit_uint(val)
		pay = builder.build()
		self.client.write_registers(reg, pay, skip_encode=True, slave=self.slaveaddr)
		
	def __read_u32(self, reg):
		result = self.client.read_holding_registers(reg, 2,  slave=self.slaveaddr)
		decoder = payload.BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=constants.Endian.BIG, wordorder=constants.Endian.LITTLE)
		return decoder.decode_32bit_uint()

	target_voltage = property(lambda self: self.__read_u32(0x0100)/1000000.0, lambda self, val: self.__write_u32(0x0100, int(float(val)*1000000)))
	target_current = property(lambda self: self.__read_u32(0x0102), lambda self, val: self.__write_u32(0x0102, int(float(val)*1000000)))
	target_mode = property(lambda self: self.Mode(self.__read_u16(0x0106)), lambda self, val: self.__write_u16(0x0106, val.value))
	target_time = property(lambda self: self.__read_u32(0x0107), lambda self, val: self.__write_u32(0x0107, int(val)))
	target_enable = property(lambda self: self.__read_u16(0x0109), lambda self, val: self.__write_u16(0x0109, val))
	
	state_voltage = property(lambda self: self.__read_u32(0x0200)/1000000.0, None)
	state_current = property(lambda self: self.__read_u32(0x0202)/1000000.0, None)
	state_time = property(lambda self: self.__read_u32(0x0208), None)
	state_input_voltage = property(lambda self: self.__read_u32(0x020C)/1000000.0, None)
	state_temperature = property(lambda self: self.__read_i16(0x020E)/10.0, None)
	state_status = property(lambda self: self.Status(self.__read_u16(0x020F)), None)


if __name__ == '__main__':
	ap = argparse.ArgumentParser()
	ap.add_argument('-i', '--ipaddr', required=True, help='Device IP address')
	ap.add_argument('-v', '--voltage', required=True, help='voltag', type=float)
	ap.add_argument('-c', '--current', required=True, help='current', type=float)
	ap.add_argument('-t', '--time', help='time')
	ap.add_argument('-w', help='Wait', action='store_true')
	args = ap.parse_args()
	
	ps = Ps3604l(args.ipaddr)
	ps.target_voltage = args.voltage
	ps.target_current = args.current
	if args.time:
		ps.target_time = args.time
		ps.target_mode = ps.Mode.timeShutdown
	else:
		ps.target_mode = ps.Mode.limitation
	ps.target_enable = 1

	while True:
		try:
			clear = '\x1b[2K'
			print(clear, 'voltage: {} | current: {} | time: {} | mode: {} | enable: {} | temperature {} | {}'.format(
				ps.state_voltage, ps.state_current, ps.state_time, ps.target_mode, ps.target_enable, ps.state_temperature, ps.state_status), end='\r')
			time.sleep(0.1)
		
		except KeyboardInterrupt:
			ps.target_enable = 0
			print(clear)
			break
