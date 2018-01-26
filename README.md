# candelapy
*candelapy* is a simple python script that lets you control your Yeelight Candela Ambient Lamp YLFW01YL over BLE.

Requirements
------------

*candelapy* is based on *pygatt*:

    $ sudo pip install pygatt
    
If you want to use the webserver version you'll need *Flask*

    $ sudo pip3 install flask
    
Installation
------------

    $ git clone git://github.com/praschak/candelapy.git
    
Usage
-----

To control your lamps(s) you need to find out their MAC adress. Usually they are listed as *yeelight_ms*.

    $ sudo hcitool lescan

Afterwards you can use the script as follows:

    $ python candelapy.py [mac adress] [intensity 0-100]
    
The webserver versions can be accessed via Port 5000:

    http://[IP]:5000/yeelight?intensity=[intensity 0-100]
    
Examples
--------

To turn on the lamp to full intensity:

    $ python candelapy.py F8:24:41:C0:71:A7 100
    
And to turn off the lamp:

    $ python candelapy.py F8:24:41:C0:71:A7 0
    
Simple integration into Home Assistant:

    switch:
      platform: command_line
       switches:
        light_bathroom:
          friendly_name: 'Light Bathroom'
          command_on: 'python /home/pi/candelapy.py F8:24:41:C0:71:A7 100'
          command_off: 'python /home/pi/candelapy.py F8:24:41:C0:71:A7 0'
    
Open Tasks
----------
- Activating the Fire-Mode and controlling several lamps (BLE mash) at once is not yet implemented in the official app, thus not reverse engineerable.
