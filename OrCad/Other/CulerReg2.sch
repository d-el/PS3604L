*version 9.2 2854699223
u 890
V? 23
C? 11
R? 28
Q? 4
S? 6
? 7
U? 2
M? 3
@libraries
@analysis
.TRAN 1 0 0 0
+0 20ns
+1 30ms
.STEP 0 0 3
+ 1 Resistor
+ 2 R24
+ 3 Value
+ 4 100
+ 5 10
+ 6 -1
.OP 0 
@targets
@attributes
@translators
a 0 u 13 0 0 0 hln 100 PCBOARDS=PCB
a 0 u 13 0 0 0 hln 100 PSPICE=PSPICE
a 0 u 13 0 0 0 hln 100 XILINX=XILINX
@setup
unconnectedPins 0
connectViaLabel 0
connectViaLocalLabels 0
NoStim4ExtIFPortsWarnings 1
AutoGenStim4ExtIFPorts 1
@index
pageloc 1 0 7474 
@status
c 116:07:09:01:20:33;1470694833
n 0 116:07:09:01:20:36;1470694836 e 
s 2832 116:08:29:20:01:22;1475168482 e 
*page 1 0 1520 970 iB
@ports
port 4 GND_ANALOG 250 260 h
port 97 GND_ANALOG 290 260 h
port 284 GND_ANALOG 490 220 h
port 465 +5V 250 200 h
a 1 x 3 0 0 0 hcn 100 LABEL=+12V
port 369 GND_ANALOG 420 370 h
port 466 +5V 480 280 u
a 1 x 3 0 -6 10 hcn 100 LABEL=+12V
port 677 GND_ANALOG 670 420 h
port 780 GND_ANALOG 350 370 h
port 853 GND_ANALOG 610 420 h
port 883 GND_ANALOG 850 530 h
port 884 GND_ANALOG 890 530 h
port 885 GND_ANALOG 940 450 h
@parts
part 2 VDC 250 210 h
a 1 u 13 0 -11 18 hcn 100 DC=12V
a 1 ap 9 0 28 17 hcn 100 REFDES=V1
a 0 sp 0 0 22 37 hln 100 PART=VDC
a 0 a 0:13 0 0 0 hln 100 PKGREF=V1
part 91 c 290 220 d
a 0 sp 0 0 0 10 hlb 100 PART=c
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=CK05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 u 13 0 23 -3 hln 100 VALUE=10u
a 0 a 0:13 0 0 0 hln 100 PKGREF=C3
a 0 ap 9 0 15 -4 hln 100 REFDES=C3
part 264 LMC7101A/NS 440 270 U
a 0 sp 11 0 124 64 hln 100 PART=LMC7101A/NS
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP8
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=U1
a 0 ap 9 0 80 44 hln 100 REFDES=U1
part 743 IRFP9140 580 250 U
a 0 sp 11 0 10 40 hcn 100 PART=IRFP9140
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=TO-247AC
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=M2
a 0 ap 9 0 5 10 hcn 100 REFDES=M2
part 671 R 670 360 d
a 0 u 13 0 21 1 hln 100 VALUE=100
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=R24
a 0 ap 9 0 11 0 hln 100 REFDES=R24
part 290 R 520 320 u
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=R12
a 0 ap 9 0 39 26 hln 100 REFDES=R12
a 0 u 13 0 13 27 hln 100 VALUE=33k
part 291 R 420 370 v
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=R13
a 0 ap 9 0 13 38 hln 100 REFDES=R13
a 0 u 13 0 23 37 hln 100 VALUE=10k
part 852 c 610 380 d
a 0 sp 0 0 0 10 hlb 100 PART=c
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=CK05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=C10
a 0 ap 9 0 15 -4 hln 100 REFDES=C10
a 0 u 13 0 27 -3 hln 100 VALUE=47u
part 879 VDC 890 490 h
a 0 sp 0 0 22 37 hln 100 PART=VDC
a 1 u 13 0 27 28 hcn 100 DC=2V
a 0 a 0:13 0 0 0 hln 100 PKGREF=V21
a 1 ap 9 0 26 19 hcn 100 REFDES=V21
part 880 Sbreak 900 420 h
a 0 s 13 0 10 -9 hln 100 MODEL=Sbreak
a 0 a 0:13 0 0 0 hln 100 PKGREF=S5
a 0 ap 9 0 10 2 hln 100 REFDES=S5
part 881 VPULSE 850 490 h
a 1 u 0 0 0 0 hcn 100 V1=0
a 1 u 0 0 0 0 hcn 100 V2=5
a 1 u 0 0 0 0 hcn 100 TD=0us
a 1 u 0 0 0 0 hcn 100 TR=5us
a 1 u 0 0 0 0 hcn 100 TF=5us
a 1 u 0 0 0 0 hcn 100 PER=10ms
a 1 u 0 0 0 0 hcn 100 PW=5ms
a 0 a 0:13 0 0 0 hln 100 PKGREF=V22
a 1 ap 9 0 20 10 hcn 100 REFDES=V22
part 578 c 490 350 h
a 0 sp 0 0 0 10 hlb 100 PART=c
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=CK05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=C7
a 0 ap 9 0 -3 2 hln 100 REFDES=C7
a 0 u 13 0 15 1 hln 100 VALUE=100p
part 882 R 720 360 d
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 u 13 0 29 -3 hln 100 VALUE=20
a 0 a 0:13 0 0 0 hln 100 PKGREF=R27
a 0 ap 9 0 11 -2 hln 100 REFDES=R27
part 788 VDC 350 330 h
a 0 sp 0 0 22 37 hln 100 PART=VDC
a 0 a 0:13 0 0 0 hln 100 PKGREF=V20
a 1 ap 9 0 28 17 hcn 100 REFDES=V20
a 1 u 13 0 27 30 hcn 100 DC=2V
part 1 titleblk 1520 970 h
a 1 s 13 0 350 10 hcn 100 PAGESIZE=B
a 1 s 13 0 180 60 hcn 100 PAGETITLE=
a 1 s 13 0 340 95 hrn 100 PAGECOUNT=1
a 1 s 13 0 300 95 hrn 100 PAGENO=1
part 886 nodeMarker 850 420 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 s 0 0 0 0 hln 100 PROBEVAR=R7:1
a 0 a 0 0 4 22 hlb 100 LABEL=4
part 319 nodeMarker 670 340 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=R24:1
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 s 0 0 0 0 hln 100 PROBEVAR=R18:1
a 0 s 0 0 0 0 hln 100 PROBEVAR=R14:1
a 0 a 0 0 4 22 hlb 100 LABEL=5
part 889 iMarker 720 360 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 6 20 hlb 100 LABEL=6
@conn
w 112
a 0 up 0:33 0 0 0 hln 100 V=
s 250 260 250 250 113
a 0 up 33 0 252 265 hlt 100 V=
w 183
a 0 up 0:33 0 0 0 hln 100 V=
s 290 260 290 250 182
a 0 up 33 0 292 255 hlt 100 V=
w 464
a 0 up 0:33 0 0 0 hln 100 V=
s 480 220 490 220 463
a 0 up 33 0 485 219 hct 100 V=
w 676
a 0 up 0:33 0 0 0 hln 100 V=
s 670 400 670 420 706
a 0 up 33 0 672 405 hlt 100 V=
w 361
a 0 up 0:33 0 0 0 hln 100 V=
s 250 200 290 200 265
a 0 up 33 0 380 199 hct 100 V=
s 290 220 290 200 95
s 250 200 250 210 17
s 290 200 610 200 456
s 610 200 610 230 267
w 468
a 0 up 0:33 0 0 0 hln 100 V=
s 580 250 520 250 748
a 0 up 33 0 555 249 hct 100 V=
w 580
a 0 up 0:33 0 0 0 hln 100 V=
s 350 230 440 230 514
a 0 up 33 0 395 229 hct 100 V=
s 350 330 350 230 574
a 0 up 33 0 352 320 hlt 100 V=
w 849
a 0 up 0:33 0 0 0 hln 100 V=
s 610 420 610 410 848
a 0 up 33 0 612 415 hlt 100 V=
w 596
a 0 up 0:33 0 0 0 hln 100 V=
s 420 270 440 270 504
s 420 330 420 320 502
s 420 320 420 270 845
s 480 320 460 320 830
a 0 up 33 0 440 319 hct 100 V=
s 460 320 420 320 847
s 460 350 460 320 599
s 490 350 460 350 597
w 858
a 0 up 0:33 0 0 0 hln 100 V=
s 900 430 890 430 857
s 890 430 890 490 859
a 0 up 33 0 892 460 hlt 100 V=
w 862
a 0 up 0:33 0 0 0 hln 100 V=
s 940 450 940 430 861
a 0 up 33 0 940 409 hct 100 V=
w 864
a 0 up 0:33 0 0 0 hln 100 V=
s 720 400 720 410 863
s 720 410 760 410 865
s 940 380 940 420 867
a 0 up 33 0 942 400 hlt 100 V=
s 940 380 760 380 869
a 0 up 33 0 850 379 hct 100 V=
s 760 380 760 410 871
w 874
a 0 up 0:33 0 0 0 hln 100 V=
s 900 420 850 420 873
s 850 420 850 490 875
a 0 up 33 0 852 455 hlt 100 V=
w 824
a 0 up 0:33 0 0 0 hln 100 V=
s 610 340 610 320 374
a 0 up 33 0 685 339 hct 100 V=
s 670 360 670 340 672
s 610 340 670 340 796
s 610 320 610 270 838
s 520 320 540 320 833
a 0 up 33 0 585 319 hct 100 V=
s 540 320 610 320 840
s 540 350 540 320 825
s 610 380 610 340 850
s 520 350 540 350 823
s 720 340 720 360 877
s 720 340 670 340 887
@junction
j 250 260
+ s 4
+ w 112
j 290 260
+ s 97
+ w 183
j 480 220
+ p 264 V-
+ w 464
j 490 220
+ s 284
+ w 464
j 480 280
+ s 466
+ p 264 V+
j 420 370
+ p 291 1
+ s 369
j 440 230
+ p 264 -
+ w 580
j 290 250
+ p 91 2
+ w 183
j 290 220
+ p 91 1
+ w 361
j 250 250
+ p 2 -
+ w 112
j 250 210
+ p 2 +
+ w 361
j 250 200
+ s 465
+ w 361
j 290 200
+ w 361
+ w 361
j 670 420
+ s 677
+ w 676
j 520 250
+ p 264 OUT
+ w 468
j 610 230
+ p 743 s
+ w 361
j 580 250
+ p 743 g
+ w 468
j 440 270
+ p 264 +
+ w 596
j 420 330
+ p 291 2
+ w 596
j 350 370
+ p 788 -
+ s 780
j 350 330
+ p 788 +
+ w 580
j 670 400
+ p 671 2
+ w 676
j 610 270
+ p 743 d
+ w 824
j 670 360
+ p 671 1
+ w 824
j 670 340
+ p 319 pin1
+ w 824
j 610 320
+ w 824
+ w 824
j 540 320
+ w 824
+ w 824
j 420 320
+ w 596
+ w 596
j 460 320
+ w 596
+ w 596
j 520 320
+ p 290 1
+ w 824
j 480 320
+ p 290 2
+ w 596
j 610 380
+ p 852 1
+ w 824
j 610 340
+ w 824
+ w 824
j 610 410
+ p 852 2
+ w 849
j 610 420
+ s 853
+ w 849
j 490 350
+ p 578 1
+ w 596
j 520 350
+ p 578 2
+ w 824
j 890 490
+ p 879 +
+ w 858
j 900 430
+ p 880 2
+ w 858
j 940 430
+ p 880 4
+ w 862
j 940 420
+ p 880 3
+ w 864
j 900 420
+ p 880 1
+ w 874
j 850 490
+ p 881 +
+ w 874
j 720 400
+ p 882 2
+ w 864
j 850 530
+ s 883
+ p 881 -
j 890 530
+ s 884
+ p 879 -
j 940 450
+ s 885
+ w 862
j 850 420
+ p 886 pin1
+ w 874
j 720 360
+ p 882 1
+ w 824
j 720 360
+ p 889 pin1
+ p 882 1
j 720 360
+ p 889 pin1
+ w 824
@attributes
a 0 s 0:13 0 0 0 hln 100 PAGETITLE=
a 0 s 0:13 0 0 0 hln 100 PAGENO=1
a 0 s 0:13 0 0 0 hln 100 PAGESIZE=B
a 0 s 0:13 0 0 0 hln 100 PAGECOUNT=1
@graphics
