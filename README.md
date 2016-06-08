BUILDING
========

Prerequisites for all platforms
-------------------------------

 * CMake 2.8.0 or later


Windows (Visual Studio)
-----------------------

 * Start a Visual Studio command prompt then:
   * `mkdir build`
   * `cd build`
   * `cmake .. -G "NMake Makefiles"`
   * `nmake`

Linux
-----

   * `mkdir build`
   * `cd build`
   * `cmake ..`
   * `make`

Want to contribute to SOEM or SOES?
-----------------------------------

If you want to contribute to SOEM or SOES you will need to sign a Contributor
License Agreement and send it to us either by e-mail or by physical mail. More
information is available in the [PDF](http://openethercatsociety.github.io/cla/cla_soem_soes.pdf).

Run ugly hack to set setpoints dynamically:
-------------------------------------------
The simple-test program reads speed setpoints from stdin.
Together with a named pipe you can echo setpoints into it, like

   * simple\_test eth0 < MYFIFO
   * echo "5000 5000" > MYFIFO
   * # OR
   * topic\_to\_stdin.py > MYFIFO

This works with a single slave in the configuration EK1100+EL2008+EL7332 with 2 DC motors on the EL7332

This is a hack though, the program should simply be a ROS node via RTT/OROCOS an the soem\_beckhoff\_drivers etc. 
