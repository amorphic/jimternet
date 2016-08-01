Title: Controlling a TOSR0x USB Relay Module Using Python
Date: 2013-05-08 10:55
Author: James 
Category: Projects
Tags: Python, Making, Tosr0x
Slug: controlling-a-tosr0x-usb-relay-module-using-python
Status: published

As part of a forthcoming project to build a computerised thermostat, I
require a means of programatically controlling a pair of [relays][] to
switch mains power.

The brains of my thermostat will be a [Raspberry Pi][]. This
credit-card-sized computer is overkill for such a project, but having
access to a complete Linux environment will make it relatively simple to
do interesting things such as produce graphs, send Twitter updates and
expose temperatures via SNMP. It also allows me to code my thermostat in
any language that I choose and in this case, I've chosen Python.

One of the Raspberry Pi's key features is its [GPIO interface][],
allowing it to control all manner of electronics. However for v1 of my
thermostat I want to focus on software rather than hardware, so I went
looking for a relay controller with a USB interface. What I found was
the TOSR0x:  
![TOSR0x][]

<!-- PELICAN_END_SUMMARY -->

The TOSR0x is an inexpensive USB relay controller board, available in
2-8 relay models from [tinyosshop.com][] as well as numerous Ebay
merchants. Mine cost \$25.99, including delivery to Australia from Hong
Kong.

According to the [tinyosshop product page][tinyosshop.com], *"The TOSR0x
module uses FT232RL USB to UART chip"* and a Windows driver for the
FT232RL is provided for download. Fortunately, recent Linux kernels also
include an FT232RL driver, meaning that plugging in the TOSR0x to a
machine running any recent distro should see it recognised correctly:

`kernel: [68596.401601] usb 3-2: FTDI USB Serial Device converter now attached to ttyUSB3`

With the TOSR0x exposed as a serial device by the OS, we can use
Python's comprehensive pySerial module to connect to the device and send
control commands. These commands are helpfully documented in decimal,
hex and ASCII on the tinyosshop website:

![TOSR0x Commands][]

So after some experimetation I've created a Python module, cunningly
named [tosr0x.py][]. This module neatly wraps up pySerial and the
various TOSR0x commands, making it trivial to plug in a TOSR0x and begin
controlling it from within a, (Linux-based) Python application.

The module is fully documented in the included [README.md][] file, but
in short it will facilitate:

-   discovery of and connection to one or more TOSR0x devices
-   connection to user-specified TOSR0x devices, (e.g. '/dev/ttyUSB3')
-   setting of relay states
-   querying of relay states

Hopefully tosr0x.py will make it easier for others to get started with
the TOSR0x. My thermostat is coming along nicely and will be the subject
of a future post. In the meantime, if you use tosr0x.py for a project of
your own I'd love to hear about it!

*Update: If you're using your tosr0x to switch mains power, check out [how to build a usb powerboard and control it with python][usb powerboard].*

  [relays]: http://en.wikipedia.org/wiki/Relays
  [Raspberry Pi]: http://raspberrypi.org
  [GPIO interface]: www.raspberrypi.org/archives/tag/gpio
  [TOSR0x]: http://www.tinyosshop.com/image/cache/data/board_modules/TOSR02-1-228x228.jpg
  [tinyosshop.com]: http://www.tinyosshop.com/index.php?route=product/product&product_id=365
  [TOSR0x Commands]: http://www.tinyosshop.com/image/data/board_modules/usbrelay4-5.jpg
  [tosr0x.py]: https://github.com/amorphic/tosr0x
  [README.md]: https://github.com/amorphic/tosr0x/blob/master/README.md
  [usb powerboard]: http://jimter.net/how-to-build-a-usb-powerboard-and-control-it-with-python
