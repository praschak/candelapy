import pygatt
import time

adapter = pygatt.GATTToolBackend()

try:
    adapter.start()
    device = adapter.connect('F8:24:41:C0:71:A9')

    # Turn lamp on
    device.char_write_handle(0x001f, bytearray([0x43, 0x40, 0x01]))

    # Set light intensity (laste byte from 0x01 to 0x64)
    device.char_write_handle(0x001f, bytearray([0x43, 0x42, 0x64]))

    # Wait for 3 seconds
    time.sleep(3)

    # Turn lamp off
    device.char_write_handle(0x001f, bytearray([0x43, 0x40, 0x02]))

finally:
    adapter.stop()
