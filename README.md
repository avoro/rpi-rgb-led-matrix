News Ticker: Controlling up to three chains of 16x32 RGB LED displays using Raspberry Pi.
==================================================

Contributers
--------

The LED-matrix library is (c) Henner Zeller <h.zeller@acm.org>, licensed with
[GNU General Public License Version 2.0].

RSS parser was initally developed by chubbyemu. 


Overview
--------
The following project utlizes three 16x32 RGB LED matrix panels that are chained
in order to display a scrolling news feed acquired from `RSS` sources.


Required Materials
-------------------
1. Raspberry Pi 3 (Ubuntu Mate)
  1.1 5V power supply
2. Adafruit 16x32 LED matrix (3)
  2.1 5V power supply
3. F-F jumper wires (13)
4. M-M jumper wires (4)
5. Female DC power supply

Connecting Raspberry to LED matrix
------------

1. Grab Raspberry Pi and note the pins
<img src="img/raspberry-pi.jpg" width="300">
2. Grab 1 Adafruit 16x32 LED matrix and note the pins
<img src="img/hub75-other.jpg" width="300">
3. Connect Rasberry
<img src="img/Wiring.png" width="300">
<img src="img/raspberry-con.jpg" width="300">
<img src="img/hub75.jpg" width="300" align="right">
4. Connect LED matrix
<img src="img/hub75-con.jpg" width="300">
5. Chain 3 displays
<img src="img/three-display-con.jpg" width="300">
6. Wire the chain
<img src="img/hot-wires.jpg" width="300">
