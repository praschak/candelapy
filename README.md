# candelapy
candelapy is a simple python script that lets you control your Yeelight Candela Ambient Lamp YLFW01YL over BLE.

Requirements
------------

candelapy is based on pygatt:

    $ sudo pip install pygatt
    
Installation
------------

    $ git-clone https://github.com/praschak/candelapy
    
Usage
-----

    $ python candelapy.py [lamps mac adress] [intensity 0-100]
    
For example to turn on the lamp to full intensity

    $ python candelapy.py F8:24:41:C0:71:A7 100
    
And to turn off the lamp

    $ python candelapy.py F8:24:41:C0:71:A 0
    
Command Line use with gattool
-----------------------------

1. Make sure your lamp is not connected to any other bluetooth device (turn off bluetooth on your phone)

2. Scan for the MAC-Adress of your lamp(s):

    $ sudo hcitool lescan

3. Open gattol and connect to device 
    $ gatttool -I
    connect F8:24:41:C0:71:A9
    Wait for "Connection successful"

4. use these commands to control the lamp:

    Turn lamp on (to previously set intensity)
    char-write-cmd 0x001f 434001000000000000000000000000000000

    Turn lamp off
    char-write-cmd 0x001f 434002000000000000000000000000000000

    Control intensity (xx = 01-64 (<01 and >64 is ignored))
    char-write-cmd 0x001f 4342xx000000000000000000000000000000
