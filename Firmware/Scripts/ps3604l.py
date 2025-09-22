#!/usr/bin/env python3
# API and command line program
# Version: 0.4

import argparse
import enum
import time
from pathlib import Path
import textwrap

from pymodbus import (
    client
)
from pymodbus.pdu import FileRecord
from tqdm import tqdm

#==============================================================================
class ModbusClient:
    def __init__(self, ip, port=502):
        self.client = client.ModbusTcpClient(ip, port=port,
                                             timeout=3,
                                             retries=3,
                                             # retry_on_empty=True,
                                             reconnect_delay=1,
                                             reconnect_delay_max=9)
        print('Connected to {}:{}'.format(ip, port))

    def __del__(self):
        self.client.close()

#==============================================================================
class Modbus:
    def __init__(self, mbclient: ModbusClient, slaveaddr: int):
        self.client = mbclient.client
        self.slaveaddr = slaveaddr

    def write_u16(self, reg, val):
        self.client.write_register(reg, val, slave=self.slaveaddr)

    def read_u16(self, reg):
        r = self.client.read_holding_registers(reg, count=1, slave=self.slaveaddr)
        return r.registers[0]

    def read_i16(self, reg):
        result = self.client.read_holding_registers(reg, count=1, slave=self.slaveaddr)
        return self.client.convert_from_registers(result.registers, data_type=self.client.DATATYPE.INT16,
                                                  word_order='little')

    def write_i16(self, reg):
        pay = self.client.convert_to_registers(val, data_type=self.client.DATATYPE.INT16)
        self.client.write_registers(reg, pay, skip_encode=True, slave=self.slaveaddr)

    def write_u32(self, reg, val):
        pay = self.client.convert_to_registers(val, data_type=self.client.DATATYPE.UINT32, word_order='little')
        self.client.write_registers(reg, pay, slave=self.slaveaddr)

    def read_u32(self, reg):
        result = self.client.read_holding_registers(reg, count=2, slave=self.slaveaddr)
        return self.client.convert_from_registers(result.registers, data_type=self.client.DATATYPE.UINT32,
                                                  word_order='little')

    def write_i32(self, reg, val):
        pay = self.client.convert_to_registers(val, data_type=self.client.DATATYPE.INT32, word_order='little')
        self.client.write_registers(reg, pay, slave=self.slaveaddr)

    def read_i32(self, reg):
        result = self.client.read_holding_registers(reg, count=2, slave=self.slaveaddr)
        return self.client.convert_from_registers(result.registers, data_type=self.client.DATATYPE.INT32,
                                                  word_order='little')

    def read_holding_registers(self, reg, count):
        return self.client.read_holding_registers(reg, count=count, slave=self.slaveaddr) 

    def writeFileRecord(self, file_number, record_number, record_data):
        record = FileRecord(file_number=1, record_number=record_number, record_data=record_data)
        self.client.write_file_record([record], slave=self.slaveaddr)

#==============================================================================
class Regulator:
    def __init__(self, modbusclient):
        self.modbus = Modbus(modbusclient, 1)

    class Mode(enum.Enum):
        overcurrentShutdown = 0
        limitation = 1
        lowCurrentShutdown = 2
        dacMode = 3

    class Crange(enum.Enum):
	    hi = 0
	    auto = 1

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
        cRangeHi = 256

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

    def readVersion(self):
        major = self.modbus.read_u16(0x0000)
        minor = self.modbus.read_u16(0x0001)
        patch = self.modbus.read_u16(0x0002)
        return major, minor, patch

    sn = property(lambda self: self.modbus.read_i32(0x0004), None)

    target_voltage = property(lambda self: self.modbus.read_i32(0x0100) / 1000000.0,
                              lambda self, val: self.modbus.write_i32(0x0100, int(float(val) * 1000000)))
    target_current = property(lambda self: self.modbus.read_i32(0x0102),
                              lambda self, val: self.modbus.write_i32(0x0102, int(float(val) * 1000000)))
    target_vdac = property(lambda self: self.modbus.read_i32(0x0104),
                              lambda self, val: self.modbus.write_i32(0x0104, int(val)))
    target_idac = property(lambda self: self.modbus.read_i32(0x0106),
                              lambda self, val: self.modbus.write_i32(0x0106, int(val)))
    target_mode = property(lambda self: self.Mode(self.modbus.read_u16(0x0108)),
                           lambda self, val: self.modbus.write_u16(0x0108, val.value))
    target_time = property(lambda self: self.modbus.read_u32(0x0109) / 1000.0,
                           lambda self, val: self.modbus.write_u32(0x0109, int(val * 1000.0)))
    target_enable = property(lambda self: self.modbus.read_u16(0x010B),
                             lambda self, val: self.modbus.write_u16(0x010B, val))
    target_wire_resistance = property(lambda self: self.modbus.read_u32(0x010C) / 10000.0,
                             lambda self, val: self.modbus.write_u32(0x010C, int(float(val) * 10000)))
    target_save_settings = property(lambda self: self.modbus.read_u16(0x010F),
                                    lambda self, val: self.modbus.write_u16(0x010F, val))
    target_crange = property(lambda self: self.Crange(self.modbus.read_u16(0x0110)),
                             lambda self, val: self.modbus.write_u16(0x0110, val.value))
    target_reboot = property(lambda self: self.modbus.read_u16(0x0111),
                             lambda self, val: self.modbus.write_u16(0x0111, val))

    state_voltage = property(lambda self: self.modbus.read_i32(0x0200) / 1000000.0, None)
    state_current = property(lambda self: self.modbus.read_i32(0x0202) / 1000000.0, None)
    state_power = property(lambda self: self.modbus.read_i32(0x0204) / 1000000.0, None)
    state_resistance = property(lambda self: self.modbus.read_i32(0x0206) / 10000.0, None)
    state_time = property(lambda self: self.modbus.read_u32(0x0208), None)
    state_capacity = property(lambda self: self.modbus.read_u32(0x020A), None)
    state_input_voltage = property(lambda self: self.modbus.read_i32(0x020C) / 1000000.0, None)
    state_temp_heatsink = property(lambda self: self.modbus.read_i16(0x020E) / 10.0, None)
    state_temp_shunt = property(lambda self: self.modbus.read_i16(0x020F) / 10.0, None)
    state_temp_ref = property(lambda self: self.modbus.read_i16(0x0210) / 10.0, None)
    state_status = property(lambda self: self.Status(self.modbus.read_u16(0x0211)), None)
    state_disablecause = property(lambda self: self.Disablecause(self.modbus.read_u16(0x0212)), None)
    state_vadc = property(lambda self: self.modbus.read_i32(0x0213), None)
    state_iadc = property(lambda self: self.modbus.read_i32(0x0215), None)

    class State():
        pass

    def getState(self):
        rr = self.modbus.read_holding_registers(0x0200, count=19) 
        s = self.State()
        s.voltage = self.modbus.client.convert_from_registers([rr.registers[1], rr.registers[0]], data_type=self.modbus.client.DATATYPE.INT32) / 1000000.0
        s.current = self.modbus.client.convert_from_registers([rr.registers[3], rr.registers[2]], data_type=self.modbus.client.DATATYPE.INT32) / 1000000.0
        s.power = self.modbus.client.convert_from_registers([rr.registers[5], rr.registers[4]], data_type=self.modbus.client.DATATYPE.INT32) / 1000000.0
        s.resistance = self.modbus.client.convert_from_registers([rr.registers[7], rr.registers[6]], data_type=self.modbus.client.DATATYPE.INT32) / 10000.0
        s.time = self.modbus.client.convert_from_registers([rr.registers[9], rr.registers[8]], data_type=self.modbus.client.DATATYPE.UINT32) / 1000.0
        s.capacity = self.modbus.client.convert_from_registers([rr.registers[11], rr.registers[10]], data_type=self.modbus.client.DATATYPE.UINT32)
        s.input_voltage = self.modbus.client.convert_from_registers([rr.registers[13], rr.registers[12]], data_type=self.modbus.client.DATATYPE.INT32) / 1000000.0
        s.state_temp_heatsink = self.modbus.client.convert_from_registers([rr.registers[14]], data_type=self.modbus.client.DATATYPE.INT16) / 10.0
        s.state_temp_shunt = self.modbus.client.convert_from_registers([rr.registers[15]], data_type=self.modbus.client.DATATYPE.INT16) / 10.0
        s.state_temp_ref = self.modbus.client.convert_from_registers([rr.registers[16]], data_type=self.modbus.client.DATATYPE.INT16) / 10.0
        s.status = self.Status(self.modbus.client.convert_from_registers([rr.registers[17]], data_type=self.modbus.client.DATATYPE.UINT16))
        s.disablecause = self.Disablecause(self.modbus.client.convert_from_registers([rr.registers[18]], data_type=self.modbus.client.DATATYPE.UINT16))
        return s

    def updateFw(self, filePath):
        data = Path(filePath).read_bytes()
        fwLen = len(data)
        pbar = tqdm(total=fwLen, desc="Loading...", unit='B')
        for offset in range(0, fwLen, 128):
            bytesToWrite = 128 if fwLen - offset >= 128 else fwLen - offset
            pbar.update(bytesToWrite)
            record_number = int(offset / 128)
            self.modbus.writeFileRecord(file_number=1, record_number=record_number,
                                        record_data=data[offset: offset + bytesToWrite])
        pbar.close()
        self.target_reboot = 1
        print('wait for boot')
        time.sleep(10)
        major, minor, patch = self.readVersion()
        print(f'New regulator version {major}.{minor}.{patch}')

#==============================================================================
class Panel(Modbus):
    def __init__(self, modbusclient):
        self.modbus = Modbus(modbusclient, 2)

    target_save_settings = property(lambda self: self.modbus.read_u16(0x010F),
                                   lambda self, val: self.modbus.write_u16(0x010F, val))
    target_reboot = property(lambda self: self.modbus.read_u16(0x0111),
                             lambda self, val: self.modbus.write_u16(0x0111, val))

    def readVersion(self):
        major = self.modbus.read_u16(0x0000)
        minor = self.modbus.read_u16(0x0001)
        patch = self.modbus.read_u16(0x0002)
        return major, minor, patch

    sn = property(lambda self: self.modbus.read_i32(0x0004), None)

    def updateFw(self, filePath):
        data = Path(filePath).read_bytes()
        fwLen = len(data)
        pbar = tqdm(total=fwLen, desc="Loading...", unit='B')
        for offset in range(0, fwLen, 128):
            bytesToWrite = 128 if fwLen - offset >= 128 else fwLen - offset
            pbar.update(bytesToWrite)
            record_number = int(offset / 128)
            self.modbus.writeFileRecord(file_number=1, record_number=record_number,
                                        record_data=data[offset: offset + bytesToWrite])
        pbar.close()
        self.target_reboot = 1
        print('wait for boot (10-20s)')
        time.sleep(2)

class Ps3604l:
    def __init__(self, ip):
        self.modbusclient = ModbusClient(ip)
        self.regulator = Regulator(self.modbusclient)
        self.panel = Panel(self.modbusclient)
        rmajor, rminor, rpatch = self.regulator.readVersion()
        pmajor, pminor, ppatch = self.panel.readVersion()
        print(f'Version P{pmajor}.{pminor}.{ppatch} R{rmajor}.{rminor}.{rpatch}, sn {self.regulator.sn}')

#==============================================================================
if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='PS3604L power supply command line interface.',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=textwrap.dedent('''\
                Example:
                    Enable 1V, 0.1A
                        ./ps3604l.py -i 192.168.88.11 -v1 -c0.1
                    Enable 1V, 0.1A, 100ms
                        ./ps3604l.py -i 192.168.88.11 -v1 -c0.1 -t0.1
                    Upgrade panel firmware:
                        ./ps3604l.py -i 192.168.88.11 -v0 -c0 -p ../Panel/build/PS3604LF_2.5.0.bin
                    Upgrade regulator firmware:
                        ./ps3604l.py -i 192.168.88.11 -v0 -c0 -r ../Regulator/build/PS3604LR_1.12.5.bin
                 '''))
    ap.add_argument('-i', '--ipaddr', required=True, help='Device IP address')
    ap.add_argument('-v', '--voltage', type=float, required=True, help='voltag')
    ap.add_argument('-c', '--current', type=float, required=True, help='current')
    ap.add_argument('-m', '--currentmeter', type=str, required=False, default='h', help='current meter range, h - high, a - auto')
    ap.add_argument('-t', '--time', type=float, help='time')
    ap.add_argument("-r", "--fwregulator", required=False, help="Firmware regulator file")
    ap.add_argument("-p", "--fwpanel", required=False, help="Firmware panel file")
    ap.add_argument('-w', help='Wait', action='store_true')
    args = ap.parse_args()

    ps = Ps3604l(args.ipaddr)

    if args.fwregulator:
        print('Do you want write firmware to regulator? [y/n]')
        resp = input()
        if resp != 'y' and resp != 'Y':
            print('Exit')
            quit()
        ps.regulator.updateFw(args.fwregulator)
        time.sleep(1)
        raise SystemExit

    if args.fwpanel:
        print('Do you want write firmware to panel? [y/n]')
        resp = input()
        if resp != 'y' and resp != 'Y':
            print('Exit')
            quit()
        ps.panel.updateFw(args.fwpanel)
        time.sleep(1)
        raise SystemExit

    ps.regulator.target_voltage = args.voltage
    ps.regulator.target_current = args.current
    ps.regulator.target_mode = ps.regulator.Mode.limitation
    ps.regulator.target_crange = ps.regulator.Crange.hi if args.currentmeter == 'h' else ps.regulator.Crange.auto
    if args.time:
        ps.regulator.target_time = args.time
    ps.regulator.target_enable = 1

    while True:
        try:
            s = ps.regulator.getState()
            lineUp='\x1B[F'

            res_str = f'{s.resistance:10.6f}' if s.resistance > 0 else '       ---'
            print('| voltage: {:7.3f}V | current: {:9.6f}A | power: {:9.6f}W | resistance: {}Ω |'.format(
                s.voltage,
                s.current,
                s.power,
                res_str)
                + ' '*20)

            print('| enable: {:9} | vdc: {:13.1f}V | time: {:10.3f}s | capacity: {:11.3f}Ah |'.format(
                ps.regulator.target_enable,
                s.input_voltage,
                s.time,
                s.capacity)
                + ' '*20, end='\n')

            print(f'| heatsink: {s.state_temp_heatsink:4.1f} °C | shunt: {s.state_temp_shunt:9.1f} °C | ref: {s.state_temp_ref:9.1f} °C | {ps.regulator.target_mode:23} |'
                + ' '*20, end='\n')

            print(f'| {s.disablecause:39} | {s.status:43} |'
                + ' '*20, end=lineUp + lineUp + lineUp)

            time.sleep(0.1)

        except KeyboardInterrupt:
            ps.regulator.target_enable = 0
            ps.regulator.target_voltage = 0
            ps.regulator.target_current = 0
            print('\n\n')
            break
