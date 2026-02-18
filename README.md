# ReadMe

This repo is a minimal one created to back up the code which was previously lost while working on the dietpi session on the pi 5. 
And this code may or may not work in the newer or fresh install of pi. I am not liable for that since systemm packages change and 
sonetimes luck just doesn't play the right part.

## What to do before running them


- don't just blindly copy the repo and run the programs or install the requirements and run them. Firstly **create a virtual environment** and then run this line:
```
pip install -r requirements.txt

```
- This will ensure your system packages and these packages don't fight with each other leading to world war 3 or the next thermo-nuclear war (which btw I am not responsible).
- Then run the programs or create newer ones as you wish.

## Important notice

This version of code was tested and run on Pi 5 with 4GB RAM (yes just 4Gb!) running Pi OS, read the detials below:

```
 Static hostname: reev
       Icon name: computer
      Machine ID: 02abda3adb7749ddaf5e2e1d264b0d24
         Boot ID: 5df33a28572f49a58de5fe56cc5ee72d
Operating System: Raspbian GNU/Linux 13 (trixie)  
          Kernel: Linux 6.12.62+rpt-rpi-v8
    Architecture: arm64

```

Board info:

```
Description        : Raspberry Pi 5B rev 1.0
Revision           : c04170
SoC                : BCM2712
RAM                : 4GB
Storage            : MicroSD
USB ports          : 4 (of which 2 USB3)
Ethernet ports     : 1 (1000Mbps max. speed)
Wi-fi              : True
Bluetooth          : True
Camera ports (CSI) : 2
Display ports (DSI): 2

,--------------------------------.
| oooooooooooooooooooo J8   : +====
| 1ooooooooooooooooooo      : |USB2
|  Wi  Pi Model 5B  V1.0  fan +====
|  Fi     +---+      +---+       |
|         |RAM|      |RP1|    +====
||p       +---+      +---+    |USB3
||c      -------              +====
||i        SoC      |c|c J14     |
(        -------  J7|s|s 12 +======
|  J2 bat   uart   1|i|i oo |   Net
| pwr\..|hd|...|hd|o|1|0    +======
`-| |-1o|m0|---|m1|--------------'

J8:
   3V3  (1) (2)  5V    
 GPIO2  (3) (4)  5V    
 GPIO3  (5) (6)  GND   
 GPIO4  (7) (8)  GPIO14
   GND  (9) (10) GPIO15
GPIO17 (11) (12) GPIO18
GPIO27 (13) (14) GND   
GPIO22 (15) (16) GPIO23
   3V3 (17) (18) GPIO24
GPIO10 (19) (20) GND   
 GPIO9 (21) (22) GPIO25
GPIO11 (23) (24) GPIO8 
   GND (25) (26) GPIO7 
 GPIO0 (27) (28) GPIO1 
 GPIO5 (29) (30) GND   
 GPIO6 (31) (32) GPIO12
GPIO13 (33) (34) GND   
GPIO19 (35) (36) GPIO16
GPIO26 (37) (38) GPIO20
   GND (39) (40) GPIO21

J2:
RUN (1)
GND (2)

J7:
COMPOSITE (1)
      GND (2)

J14:
TR01 TAP (1) (2) TR00 TAP
TR03 T

```
