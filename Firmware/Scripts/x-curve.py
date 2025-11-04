#!/usr/bin/env python3
# Measure MOSFET Output Characteristics
# Version: 0.1

from ps3604l import Ps3604l
import argparse
import time
import textwrap
import numpy      as np
import gnuplotlib as gp

# Settings
Vlimit = 30.0       # [V]
Istart = 0.025      # [A]
Iend = 3.5          # [A]
Ithreshold = 1      # [A]
Istep1 = 0.025      # [A]
Time1 = 0.3         # [s]
Istep2 = 0.05       # [A]

gate_voltage = [3.85, 3.875, 3.9, 3.925, 3.95, 3.975, 4.0, 4.025, 4.05, 4.075, 4.1] #

if __name__ == '__main__':
    # SetUp
    ap = argparse.ArgumentParser(description='I-V measure',
                                formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''\
                                Example:
                                    ./x-curve.py -i192.168.88.11 -g192.168.88.10 -n IRF3710
                                '''))

    ap.add_argument("-i", "--drainipaddr", required=True, help="IP address PS3604L for drain source")
    ap.add_argument("-g", "--gateipaddr", required=True, help="IP address PS3604L for gate source")
    ap.add_argument("-n", "--name", required=True, help="Name")
    ap.add_argument("-d", "--description", required=False, help="Description")
    args = ap.parse_args()

    try:
        # Setup PS
        ps = Ps3604l(args.drainipaddr)
        ps.regulator.target_voltage = Vlimit
        ps.regulator.target_current = Istart
        ps.regulator.target_mode = ps.regulator.Mode.limitation
        ps.regulator.target_time = 0
        ps.regulator.target_vfilter_size = 400
        ps.regulator.target_ifilter_size = 400
        ps.regulator.target_enable = 1
        
        psg = Ps3604l(args.gateipaddr)
        psg.regulator.target_voltage = gate_voltage[0]
        psg.regulator.target_current = 0.1
        psg.regulator.target_time = 0
        psg.regulator.target_enable = 1
        time.sleep(1)

        results = list()
        for gv in gate_voltage:            # Measure loop
            print("---------------------------------")
            print(f'Set gate voltage {gv}V')
            psg.regulator.target_voltage = gv
            current = Istart
            resultv = list()
            resulti = list()
            while current < Iend:
                ps.regulator.target_current = current
                if current < Ithreshold:
                    current = current + Istep1
                else:
                    current = current + Istep2
                time.sleep(Time1)
                um = ps.regulator.state_voltage
                im = ps.regulator.state_current
                resultv.append(um)
                resulti.append(im)
                print(f'Iset {ps.regulator.target_current:5.3f}A, Um {um:5.3f}V, Im {im:5.3f}A')
                
                ps.regulator.target_current = 0.001
                time.sleep(2.5)
                
            results.append((resultv, resulti))
            ps.regulator.target_current = Istart
            time.sleep(1)

        # Disable outputs
        ps.regulator.target_enable = 0
        psg.regulator.target_enable = 0

        #------------------------
        pl = list()
        for i in range(len(gate_voltage)):
            resultv, resulti = results[i]
            x = np.array(resultv)
            y = np.array(resulti)
            curve_options0 = dict(legend = f'V_G_S {gate_voltage[i]}V')
            curve0 = (x, y, curve_options0)
            pl.append(curve0)

        gp.plot(*pl,
                cmds = "set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor rgb\"#3D3846\" behind",
                ylabel  = 'I_D, Drainn-to-Source Current (A)',
                xlabel = 'V_D_S, Drain-to-Source Voltage (V)',
                title   = f"{args.name}",
                wait=True)
             
    except KeyboardInterrupt:
        ps.regulator.target_enable = 0
        psg.regulator.target_enable = 0

