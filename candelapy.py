
import pygatt
import sys

adapter = pygatt.GATTToolBackend()

# Get command line argument
intensity = int(sys.argv[1])

try:

    # Connect to lamp
    adapter.start()
    device = adapter.connect('F8:24:41:C0:71:A9')

    if intensity > 0 & intensity <= 100:

        # Turn lamp on
        device.char_write_handle(0x001f, bytearray([0x43, 0x40, 0x01]))

        # Set light intensity
        device.char_write_handle(0x001f, bytearray([0x43, 0x42, intensity]))

    if intensity <= 0:

        # Turn lamp off
        device.char_write_handle(0x001f, bytearray([0x43, 0x40, 0x02]))

finally:
    adapter.stop()
