#!/usr/bin/env python3
# API and simple console program
# version 0.1

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
		self.client = client.ModbusTcpClient(ip, port=port,
			timeout=3,
			retries=3,
			retry_on_empty=True,
			reconnect_delay=1,
			reconnect_delay_max=9)
		print('Connection to {}:{}'.format(ip, port), end=' ')
		r = self.client.read_holding_registers(0x0000, 3, slave=self.slaveaddr)
		print('Regulator version {major}.{minor}.{patch}, sn {sn}'.format(
			major=r.registers[0], minor=r.registers[1], patch=r.registers[2], sn=self.__read_u32(0x0004)))
	
	def __del__(self):
		self.client.close()
	
	class Mode(enum.Enum):
		overcurrentShutdown = 0
		limitation = 1
		lowCurrentShutdown = 3
		dacMode = 4
	
	class Status(enum.Flag):
		normal = 0
		errorExternalIAdc = 1
		errorTemperatureSensor = 2
		overheated = 4
		lowInputVoltage = 8
		reverseVoltage = 16
		notCalibrated = 32
		limitation = 64
		externaIAdc = 128
	
	class Disablecause(enum.Enum):
		none = 0
		errorTemperatureSensor = 1
		overheated = 2
		lowInputVoltage = 3
		reverseVoltage = 4
		overCurrent = 5
		timeShutdown = 6
		lowCurrentShutdown = 7
		request = 8
	
	def __write_u16(self, reg, val):
		self.client.write_register(reg, val)
		
	def __read_u16(self, reg):
		r = self.client.read_holding_registers(reg, 1, slave=self.slaveaddr)
		return r.registers[0]
	
	def __read_i16(self, reg):
		result = self.client.read_holding_registers(reg, 1,  slave=self.slaveaddr)
		decoder = payload.BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=constants.Endian.BIG, wordorder=constants.Endian.LITTLE)
		return decoder.decode_16bit_int()
	
	def __write_i16(self, reg):
		builder = payload.BinaryPayloadBuilder(byteorder=constants.Endian.BIG, wordorder=constants.Endian.LITTLE)
		builder.add_16bit_int(val)
		pay = builder.build()
		self.client.write_registers(reg, pay, skip_encode=True, slave=self.slaveaddr)

	def __write_u32(self, reg, val):
		builder = payload.BinaryPayloadBuilder(byteorder=constants.Endian.BIG, wordorder=constants.Endian.LITTLE)
		builder.add_32bit_uint(val)
		pay = builder.build()
		self.client.write_registers(reg, pay, skip_encode=True, slave=self.slaveaddr)
		
	def __read_u32(self, reg):
		result = self.client.read_holding_registers(reg, 2,  slave=self.slaveaddr)
		decoder = payload.BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=constants.Endian.BIG, wordorder=constants.Endian.LITTLE)
		return decoder.decode_32bit_uint()
		
	def __write_i32(self, reg, val):
		builder = payload.BinaryPayloadBuilder(byteorder=constants.Endian.BIG, wordorder=constants.Endian.LITTLE)
		builder.add_32bit_int(val)
		pay = builder.build()
		self.client.write_registers(reg, pay, skip_encode=True, slave=self.slaveaddr)

	def __read_i32(self, reg):
		result = self.client.read_holding_registers(reg, 2,  slave=self.slaveaddr)
		decoder = payload.BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=constants.Endian.BIG, wordorder=constants.Endian.LITTLE)
		return decoder.decode_32bit_int()

	target_voltage = property(lambda self: self.__read_i32(0x0100)/1000000.0, lambda self, val: self.__write_i32(0x0100, int(float(val)*1000000)))
	target_current = property(lambda self: self.__read_i32(0x0102), lambda self, val: self.__write_i32(0x0102, int(float(val)*1000000)))
	target_mode = property(lambda self: self.Mode(self.__read_u16(0x0108)), lambda self, val: self.__write_u16(0x0108, val.value))
	target_time = property(lambda self: self.__read_u32(0x0109)/1000.0, lambda self, val: self.__write_u32(0x0109, int(val*1000.0)))
	target_enable = property(lambda self: self.__read_u16(0x010B), lambda self, val: self.__write_u16(0x010B, val))
	
	state_voltage = property(lambda self: self.__read_i32(0x0200)/1000000.0, None)
	state_current = property(lambda self: self.__read_i32(0x0202)/1000000.0, None)
	state_power = property(lambda self: self.__read_i32(0x0204)/1000000.0, None)
	state_resistance = property(lambda self: self.__read_i32(0x0206)/1000000.0, None)
	state_time = property(lambda self: self.__read_u32(0x0208), None)
	state_input_voltage = property(lambda self: self.__read_i32(0x020C)/1000000.0, None)
	state_temperature = property(lambda self: self.__read_i16(0x020E)/10.0, None)
	state_status = property(lambda self: self.Status(self.__read_u16(0x020F)), None)
	state_disablecause = property(lambda self: self.Disablecause(self.__read_u16(0x0210)), None)
	
	class State():
		pass
	
	def getState(self):
		result = self.client.read_holding_registers(0x0200, 21,  slave=self.slaveaddr)
		decoder = payload.BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=constants.Endian.BIG, wordorder=constants.Endian.LITTLE)
		s = self.State()
		s.voltage = decoder.decode_32bit_int()/1000000.0
		s.current = decoder.decode_32bit_int()/1000000.0
		s.power = decoder.decode_32bit_uint()/1000000.0
		uresistance = decoder.decode_32bit_int()
		if uresistance == -1:
			s.resistance = float("NaN")
		else:
			s.resistance = uresistance/10000.0
		s.time = decoder.decode_32bit_uint()/1000.0
		s.capacity = decoder.decode_32bit_uint()/1000.0
		s.input_voltage = decoder.decode_32bit_int()/1000000.0
		s.temperature = decoder.decode_16bit_int()/10.0
		s.status = self.Status(decoder.decode_16bit_uint())
		s.disablecause = self.Disablecause(decoder.decode_16bit_uint())
		s.vadc = decoder.decode_16bit_uint()
		s.iadc = decoder.decode_16bit_uint()
		s.iexternaladc = decoder.decode_32bit_uint()
		return s
	

if __name__ == '__main__':
	ap = argparse.ArgumentParser(description='API PS3604L')
	ap.add_argument('-i', '--ipaddr', required=True, help='Device IP address')
	ap.add_argument('-v', '--voltage', type=float, required=True, help='voltag')
	ap.add_argument('-c', '--current', type=float, required=True, help='current')
	ap.add_argument('-t', '--time', type=float, help='time')
	ap.add_argument('-w', help='Wait', action='store_true')
	args = ap.parse_args()
	
	ps = Ps3604l(args.ipaddr)
	ps.target_voltage = args.voltage
	ps.target_current = args.current
	ps.target_mode = ps.Mode.limitation
	if args.time:
		ps.target_time = args.time
	ps.target_enable = 1

	while True:
		try:
			s = ps.getState()
			print('| voltage: {:6.3f}V | current: {:9.6f}A | power: {:6.6f}W | resistance: {:10.3f}Ω | capacity: {:12.3f}Ah | {:35} |'.format(
				s.voltage,
				s.current,
				s.power,
				s.resistance,
				s.capacity,
				s.disablecause)
				+ ' '*20)
			
			lineUp='\x1B[F'
			print('| enable: {:8} | input: {:11.1f}V | t: {:10.1f} °C | time: {:16.3f}s | {:24} | {:35} |'.format(
				ps.target_enable,
				s.input_voltage,
				s.temperature,
				s.time,
				ps.target_mode,
				s.status)
				+ ' '*20, end=lineUp)

			time.sleep(0.1)
		
		except KeyboardInterrupt:
			ps.target_enable = 0
			ps.target_voltage = 0
			ps.target_current = 0
			print('\n\n')
			break
