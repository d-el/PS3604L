*version 9.2 3319511865
u 291
V? 13
C? 6
R? 13
Q? 2
S? 4
? 5
@libraries
@analysis
.TRAN 1 0 0 0
+0 20ns
+1 100ms
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
pageloc 1 0 7729 
@status
c 116:07:08:22:53:21;1470686001
n 0 116:07:08:01:46:47;1470610007 e 
s 0 116:07:08:22:53:19;1470685999 e 
*page 1 0 1520 970 iB
@ports
port 158 GND_ANALOG 760 550 h
port 159 GND_ANALOG 800 550 h
port 161 GND_ANALOG 850 470 h
port 4 GND_ANALOG 250 260 h
port 97 GND_ANALOG 310 260 h
port 185 GND_ANALOG 590 440 h
port 83 GND_ANALOG 350 320 h
port 258 GND_ANALOG 490 360 h
port 288 GND_ANALOG 390 530 h
port 289 GND_ANALOG 430 530 h
port 290 GND_ANALOG 330 530 h
@parts
part 152 VDC 800 510 h
a 1 ap 9 0 26 19 hcn 100 REFDES=V7
a 0 sp 0 0 22 37 hln 100 PART=VDC
a 1 u 13 0 27 28 hcn 100 DC=2V
a 0 a 0:13 0 0 0 hln 100 PKGREF=V7
part 153 Sbreak 810 440 h
a 0 ap 9 0 10 2 hln 100 REFDES=S2
a 0 s 13 0 10 -9 hln 100 MODEL=Sbreak
a 0 a 0:13 0 0 0 hln 100 PKGREF=S2
part 2 VDC 250 210 h
a 1 ap 9 0 28 17 hcn 100 REFDES=V1
a 0 sp 0 0 22 37 hln 100 PART=VDC
a 0 a 0:13 0 0 0 hln 100 PKGREF=V1
a 1 u 13 0 29 28 hcn 100 DC=12V
part 91 c 310 220 d
a 0 sp 0 0 0 10 hlb 100 PART=c
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=CK05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 u 13 0 23 -3 hln 100 VALUE=10u
a 0 a 0:13 0 0 0 hln 100 PKGREF=C3
a 0 ap 9 0 15 -4 hln 100 REFDES=C3
part 155 VPULSE 760 510 h
a 1 u 0 0 0 0 hcn 100 V1=0
a 1 u 0 0 0 0 hcn 100 V2=5
a 1 u 0 0 0 0 hcn 100 TD=0us
a 1 u 0 0 0 0 hcn 100 TR=5us
a 1 u 0 0 0 0 hcn 100 TF=5us
a 0 a 0:13 0 0 0 hln 100 PKGREF=V8
a 1 ap 9 0 20 10 hcn 100 REFDES=V8
a 1 u 0 0 0 0 hcn 100 PER=10ms
a 1 u 0 0 0 0 hcn 100 PW=5ms
part 121 R 630 380 d
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=R5
a 0 ap 9 0 11 -2 hln 100 REFDES=R5
a 0 u 13 0 29 -3 hln 100 VALUE=20
part 184 R 590 380 d
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=R7
a 0 ap 9 0 11 -2 hln 100 REFDES=R7
a 0 u 13 0 29 -3 hln 100 VALUE=200
part 7 BC817-16/PLP 510 260 h
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=SOT23
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=Q1
a 0 ap 9 0 1 6 hln 100 REFDES=Q1
a 0 sp 11 0 32 6 hln 100 PART=BC817-16/PLP
part 249 c 490 300 d
a 0 sp 0 0 0 10 hlb 100 PART=c
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=CK05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=C5
a 0 ap 9 0 15 -4 hln 100 REFDES=C5
a 0 u 13 0 23 -3 hln 100 VALUE=10u
part 82 VPULSE 350 280 h
a 1 u 0 0 0 0 hcn 100 V1=0
a 1 u 0 0 0 0 hcn 100 TD=0us
a 0 a 0:13 0 0 0 hln 100 PKGREF=V6
a 1 ap 9 0 20 10 hcn 100 REFDES=V6
a 1 u 0 0 0 0 hcn 100 V2=11.5
a 1 u 0 0 0 0 hcn 100 TR=0.1us
a 1 u 0 0 0 0 hcn 100 TF=0.1us
a 1 u 0 0 0 0 hcn 100 PER=10us
a 1 u 0 0 0 0 hcn 100 PW=10us
part 6 R 470 260 u
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=R1
a 0 ap 9 0 27 36 hln 100 REFDES=R1
a 0 u 13 0 9 35 hln 100 VALUE=10
part 284 VDC 390 470 h
a 0 sp 0 0 22 37 hln 100 PART=VDC
a 1 u 13 0 27 28 hcn 100 DC=2V
a 0 a 0:13 0 0 0 hln 100 PKGREF=V11
a 1 ap 9 0 26 19 hcn 100 REFDES=V11
part 285 VPULSE 430 470 h
a 1 u 0 0 0 0 hcn 100 V1=0
a 1 u 0 0 0 0 hcn 100 V2=5
a 1 u 0 0 0 0 hcn 100 TD=0us
a 1 u 0 0 0 0 hcn 100 PER=3ms
a 1 u 0 0 0 0 hcn 100 PW=1.5ms
a 1 u 0 0 0 0 hcn 100 TR=0us
a 1 u 0 0 0 0 hcn 100 TF=0us
a 0 a 0:13 0 0 0 hln 100 PKGREF=V12
a 1 ap 9 0 20 10 hcn 100 REFDES=V12
part 286 Sbreak 380 450 H
a 0 s 13 0 -20 1 hln 100 MODEL=Sbreak
a 0 a 0:13 0 0 0 hln 100 PKGREF=S3
a 0 ap 9 0 10 2 hln 100 REFDES=S3
part 287 R 330 470 d
a 0 u 13 0 21 1 hln 100 VALUE=100
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=R12
a 0 ap 9 0 11 0 hln 100 REFDES=R12
part 1 titleblk 1520 970 h
a 1 s 13 0 350 10 hcn 100 PAGESIZE=B
a 1 s 13 0 180 60 hcn 100 PAGETITLE=
a 1 s 13 0 340 95 hrn 100 PAGECOUNT=1
a 1 s 13 0 300 95 hrn 100 PAGENO=1
part 109 iMarker 250 250 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 s 0 0 0 0 hln 100 PROBEVAR=-I(V1)
a 0 a 0 0 6 20 hlb 100 LABEL=3
part 216 nodeMarker 760 440 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 s 0 0 0 0 hln 100 PROBEVAR=R7:1
a 0 a 0 0 4 22 hlb 100 LABEL=4
part 114 nodeMarker 560 360 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 s 0 0 0 0 hln 100 PROBEVAR=R7:1
a 0 a 0 0 4 22 hlb 100 LABEL=4
@conn
w 143
a 0 up 0:33 0 0 0 hln 100 V=
s 810 450 800 450 142
s 800 450 800 510 144
a 0 up 33 0 802 480 hlt 100 V=
w 147
a 0 up 0:33 0 0 0 hln 100 V=
s 850 470 850 450 146
a 0 up 33 0 850 429 hct 100 V=
w 126
a 0 up 0:33 0 0 0 hln 100 V=
s 630 420 630 430 127
s 630 430 670 430 129
s 850 400 850 440 148
a 0 up 33 0 852 420 hlt 100 V=
s 850 400 670 400 165
s 670 400 670 430 167
w 178
a 0 up 0:33 0 0 0 hln 100 V=
s 530 200 310 200 15
a 0 up 33 0 380 199 hct 100 V=
s 530 240 530 200 13
s 310 200 250 200 180
s 310 220 310 200 95
s 250 200 250 210 17
w 112
a 0 up 0:33 0 0 0 hln 100 V=
s 250 260 250 250 113
a 0 up 33 0 252 265 hlt 100 V=
w 183
a 0 up 0:33 0 0 0 hln 100 V=
s 310 260 310 250 182
a 0 up 33 0 312 255 hlt 100 V=
w 187
a 0 up 0:33 0 0 0 hln 100 V=
s 590 440 590 420 188
a 0 up 33 0 592 430 hlt 100 V=
w 139
a 0 up 0:33 0 0 0 hln 100 V=
s 810 440 760 440 138
s 760 440 760 510 140
a 0 up 33 0 762 475 hlt 100 V=
w 257
a 0 up 0:33 0 0 0 hln 100 V=
s 490 330 490 360 253
a 0 up 33 0 492 345 hlt 100 V=
w 85
a 0 up 0:33 0 0 0 hln 100 V=
s 350 260 350 280 88
s 350 260 430 260 86
a 0 up 33 0 390 259 hct 100 V=
w 246
a 0 up 0:33 0 0 0 hln 100 V=
s 490 260 510 260 252
s 490 300 490 260 250
a 0 up 33 0 492 280 hlt 100 V=
s 470 260 490 260 8
a 0 up 33 0 470 259 hct 100 V=
w 254
a 0 up 0:33 0 0 0 hln 100 V=
s 530 360 560 360 122
s 630 360 630 380 124
s 590 360 630 360 192
a 0 up 33 0 610 359 hct 100 V=
s 590 380 590 360 190
s 560 360 590 360 193
s 530 360 530 280 241
a 0 up 33 0 532 310 hlt 100 V=
w 263
s 430 450 430 470 262
s 380 450 430 450 264
a 0 up 33 0 405 449 hct 100 V=
w 267
s 390 460 380 460 266
a 0 up 33 0 385 459 hct 100 V=
s 390 470 390 460 268
a 0 up 33 0 392 465 hlt 100 V=
w 271
s 390 530 390 510 270
a 0 up 33 0 392 520 hlt 100 V=
w 273
s 430 530 430 510 272
a 0 up 33 0 432 520 hlt 100 V=
w 275
s 330 530 330 510 274
a 0 up 33 0 332 520 hlt 100 V=
w 277
s 340 450 330 450 276
s 330 460 340 460 278
s 330 470 330 460 280
a 0 up 33 0 332 465 hlt 100 V=
s 330 450 330 460 282
a 0 up 33 0 332 455 hlt 100 V=
@junction
j 630 420
+ p 121 2
+ w 126
j 800 510
+ p 152 +
+ w 143
j 810 440
+ p 153 1
+ w 139
j 810 450
+ p 153 2
+ w 143
j 760 510
+ p 155 +
+ w 139
j 760 550
+ s 158
+ p 155 -
j 800 550
+ s 159
+ p 152 -
j 850 450
+ p 153 4
+ w 147
j 850 470
+ s 161
+ w 147
j 850 440
+ p 153 3
+ w 126
j 250 250
+ p 2 -
+ p 109 pin1
j 310 220
+ p 91 1
+ w 178
j 310 200
+ w 178
+ w 178
j 250 210
+ p 2 +
+ w 178
j 250 250
+ p 2 -
+ w 112
j 250 260
+ s 4
+ w 112
j 250 250
+ p 109 pin1
+ w 112
j 310 250
+ p 91 2
+ w 183
j 310 260
+ s 97
+ w 183
j 590 420
+ p 184 2
+ w 187
j 590 440
+ s 185
+ w 187
j 590 360
+ w 254
+ w 254
j 760 440
+ p 216 pin1
+ w 139
j 350 320
+ p 82 -
+ s 83
j 630 380
+ p 121 1
+ w 254
j 590 380
+ p 184 1
+ w 254
j 560 360
+ p 114 pin1
+ w 254
j 490 360
+ s 258
+ w 257
j 490 330
+ p 249 2
+ w 257
j 530 240
+ p 7 C
+ w 178
j 530 280
+ p 7 E
+ w 254
j 430 260
+ p 6 2
+ w 85
j 470 260
+ p 6 1
+ w 246
j 350 280
+ p 82 +
+ w 85
j 510 260
+ p 7 B
+ w 246
j 490 300
+ p 249 1
+ w 246
j 490 260
+ w 246
+ w 246
j 330 460
+ w 277
+ w 277
j 390 470
+ p 284 +
+ w 267
j 390 510
+ p 284 -
+ w 271
j 430 470
+ p 285 +
+ w 263
j 430 510
+ p 285 -
+ w 273
j 380 450
+ p 286 1
+ w 263
j 380 460
+ p 286 2
+ w 267
j 340 450
+ p 286 3
+ w 277
j 340 460
+ p 286 4
+ w 277
j 330 510
+ p 287 2
+ w 275
j 330 470
+ p 287 1
+ w 277
j 390 530
+ s 288
+ w 271
j 430 530
+ s 289
+ w 273
j 330 530
+ s 290
+ w 275
@attributes
a 0 s 0:13 0 0 0 hln 100 PAGETITLE=
a 0 s 0:13 0 0 0 hln 100 PAGENO=1
a 0 s 0:13 0 0 0 hln 100 PAGESIZE=B
a 0 s 0:13 0 0 0 hln 100 PAGECOUNT=1
@graphics
