*version 9.2 757758512
u 218
M? 4
C? 3
R? 6
V? 5
? 4
D? 4
U? 2
@libraries
@analysis
.TRAN 1 0 0 0
+0 20n
+1 15m
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
pageloc 1 0 5869 
@status
n 0 116:08:29:20:54:08;1475171648 e 
s 0 116:08:29:20:54:08;1475171648 e 
c 116:08:29:20:54:21;1475171661
*page 1 0 1520 970 iB
@ports
port 44 GND_ANALOG 700 250 h
port 105 GND_ANALOG 580 350 h
port 6 GND_ANALOG 750 250 h
port 135 GND_ANALOG 720 360 h
port 19 GND_ANALOG 380 240 h
port 76 GND_ANALOG 410 240 h
port 190 GND_ANALOG 470 200 h
port 188 GND_ANALOG 620 200 v
@parts
part 5 R 750 190 d
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=R1
a 0 ap 9 0 11 0 hln 100 REFDES=R1
a 0 u 13 0 21 1 hln 100 VALUE=2
part 36 c 700 190 d
a 0 sp 0 0 0 10 hlb 100 PART=c
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=CK05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=C2
a 0 ap 9 0 15 -4 hln 100 REFDES=C2
a 0 u 13 0 27 -3 hln 100 VALUE=1u
part 118 R 680 320 d
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 u 13 0 21 1 hln 100 VALUE=47k
a 0 a 0:13 0 0 0 hln 100 PKGREF=R4
a 0 ap 9 0 11 0 hln 100 REFDES=R4
part 134 VDC 720 320 h
a 0 sp 0 0 22 37 hln 100 PART=VDC
a 0 a 0:13 0 0 0 hln 100 PKGREF=V2
a 1 ap 9 0 26 19 hcn 100 REFDES=V2
a 1 u 13 0 27 28 hcn 100 DC=10V
part 87 LM358 640 330 V
a 0 sp 11 0 0 70 hln 100 PART=LM358
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP8
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U1
a 0 ap 9 0 14 0 hln 100 REFDES=U1A
part 18 VSIN 380 180 h
a 1 u 0 0 0 0 hcn 100 VOFF=0
a 0 a 0:13 0 0 0 hln 100 PKGREF=V1
a 1 ap 9 0 20 10 hcn 100 REFDES=V1
a 1 u 0 0 0 0 hcn 100 FREQ=1000
a 1 u 0 0 0 0 hcn 100 VAMPL=14.1V
part 75 R 410 180 d
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 u 13 0 21 1 hln 100 VALUE=20
a 0 a 0:13 0 0 0 hln 100 PKGREF=R2
a 0 ap 9 0 11 0 hln 100 REFDES=R2
part 72 120NQ045 380 170 v
a 0 sp 11 0 -5 23 hln 100 PART=120NQ045
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=D-67
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=D2
a 0 ap 9 0 0 0 hln 100 REFDES=D2
part 189 VDC 470 160 h
a 0 sp 0 0 22 37 hln 100 PART=VDC
a 1 u 13 0 27 28 hcn 100 DC=10V
a 0 a 0:13 0 0 0 hln 100 PKGREF=V4
a 1 ap 9 0 26 19 hcn 100 REFDES=V4
part 111 R 550 240 d
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=R3
a 0 ap 9 0 11 0 hln 100 REFDES=R3
a 0 u 13 0 21 1 hln 100 VALUE=47k
part 55 IRFP9140 620 170 V
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=TO-247AC
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=M3
a 0 sp 11 0 38 38 hcn 100 PART=IRFP9140
a 0 ap 9 0 49 24 hcn 100 REFDES=M3
part 148 R 620 200 d
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 u 13 0 21 1 hln 100 VALUE=47k
a 0 a 0:13 0 0 0 hln 100 PKGREF=R5
a 0 ap 9 0 11 0 hln 100 REFDES=R5
part 1 titleblk 1520 970 h
a 1 s 13 0 350 10 hcn 100 PAGESIZE=B
a 1 s 13 0 180 60 hcn 100 PAGETITLE=
a 1 s 13 0 340 95 hrn 100 PAGECOUNT=1
a 1 s 13 0 300 95 hrn 100 PAGENO=1
part 29 nodeMarker 750 140 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=2
part 28 nodeMarker 480 140 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 s 0 0 0 0 hln 100 PROBEVAR=M3:d
a 0 a 0 0 4 22 hlb 100 LABEL=1
@conn
w 81
a 0 up 0:33 0 0 0 hln 100 V=
s 700 250 700 220 47
a 0 up 33 0 702 235 hlt 100 V=
w 109
a 0 up 0:33 0 0 0 hln 100 V=
s 580 290 590 290 108
s 580 350 580 290 106
a 0 up 33 0 582 320 hlt 100 V=
w 91
a 0 up 0:33 0 0 0 hln 100 V=
s 750 230 750 250 7
a 0 up 33 0 752 235 hlt 100 V=
w 173
a 0 up 0:33 0 0 0 hln 100 V=
s 640 360 640 330 171
s 640 360 680 360 90
a 0 up 33 0 660 359 hct 100 V=
w 141
a 0 up 0:33 0 0 0 hln 100 V=
s 720 320 720 290 142
s 720 290 650 290 144
a 0 up 33 0 685 289 hct 100 V=
w 110
a 0 up 0:33 0 0 0 hln 100 V=
s 550 280 550 340 115
a 0 up 33 0 552 310 hlt 100 V=
s 600 340 600 330 182
s 600 340 550 340 98
w 153
a 0 up 0:33 0 0 0 hln 100 V=
s 620 240 620 250 151
a 0 up 33 0 622 245 hlt 100 V=
w 74
a 0 up 0:33 0 0 0 hln 100 V=
s 410 220 410 240 73
a 0 up 33 0 412 225 hlt 100 V=
w 65
a 0 up 0:33 0 0 0 hln 100 V=
s 380 180 380 170 64
a 0 up 33 0 382 175 hlt 100 V=
w 25
a 0 up 0:33 0 0 0 hln 100 V=
s 380 220 380 240 26
a 0 up 33 0 382 230 hlt 100 V=
w 196
a 0 up 0:33 0 0 0 hln 100 V=
s 380 140 410 140 191
s 410 180 410 140 77
a 0 up 33 0 412 160 hlt 100 V=
w 162
a 0 up 0:33 0 0 0 hln 100 V=
s 700 140 750 140 51
s 700 190 700 140 40
s 750 140 750 190 11
s 680 140 700 140 176
s 680 320 680 140 97
a 0 up 33 0 682 230 hlt 100 V=
s 640 140 680 140 206
w 150
a 0 up 0:33 0 0 0 hln 100 V=
s 470 160 470 140 197
s 480 140 550 140 34
a 0 up 33 0 530 139 hct 100 V=
s 550 240 550 140 112
s 470 140 480 140 199
s 550 140 600 140 204
w 213
a 0 up 0:33 0 0 0 hln 100 V=
s 620 180 620 170 186
@junction
j 700 250
+ s 44
+ w 81
j 750 250
+ s 6
+ w 91
j 700 220
+ p 36 2
+ w 81
j 750 230
+ p 5 2
+ w 91
j 720 360
+ s 135
+ p 134 -
j 590 290
+ p 87 V-
+ w 109
j 580 350
+ s 105
+ w 109
j 700 140
+ w 162
+ w 162
j 750 190
+ p 5 1
+ w 162
j 750 140
+ p 29 pin1
+ w 162
j 700 190
+ p 36 1
+ w 162
j 640 330
+ p 87 +
+ w 173
j 680 360
+ p 118 2
+ w 173
j 680 320
+ p 118 1
+ w 162
j 720 320
+ p 134 +
+ w 141
j 650 290
+ p 87 V+
+ w 141
j 550 280
+ p 111 2
+ w 110
j 600 330
+ p 87 -
+ w 110
j 620 240
+ p 148 2
+ w 153
j 620 250
+ p 87 OUT
+ w 153
j 620 200
+ s 188
+ p 148 1
j 380 140
+ p 72 K
+ w 196
j 410 180
+ p 75 1
+ w 196
j 410 220
+ p 75 2
+ w 74
j 410 240
+ s 76
+ w 74
j 380 180
+ p 18 +
+ w 65
j 380 170
+ p 72 A
+ w 65
j 380 220
+ p 18 -
+ w 25
j 380 240
+ s 19
+ w 25
j 470 200
+ p 189 -
+ s 190
j 620 170
+ p 55 g
+ w 213
j 550 140
+ w 150
+ w 150
j 640 140
+ p 55 d
+ w 162
j 680 140
+ w 162
+ w 162
j 470 160
+ p 189 +
+ w 150
j 480 140
+ p 28 pin1
+ w 150
j 550 240
+ p 111 1
+ w 150
j 600 140
+ p 55 s
+ w 150
@attributes
a 0 s 0:13 0 0 0 hln 100 PAGETITLE=
a 0 s 0:13 0 0 0 hln 100 PAGENO=1
a 0 s 0:13 0 0 0 hln 100 PAGESIZE=B
a 0 s 0:13 0 0 0 hln 100 PAGECOUNT=1
@graphics
