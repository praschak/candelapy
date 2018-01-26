
from flask import Flask
app = Flask(__name__)
import pygatt
import sys
from flask import request

adapter = pygatt.GATTToolBackend()
adapter.start()

print("Trying to connect...")

try:
 device = adapter.connect("F8:24:41:C0:71:A9")
except:
 print("Connection Error")
finally:
 device.char_write_handle(0x001f, bytearray([0x43, 0x67, 0x02]))
 print("Now turn the lamp")

@app.route("/yeelight")
def on():
 intensity = int(request.args.get('intensity'))

 if intensity > 0:
  device.char_write_handle(0x001f, bytearray([0x43, 0x40, 0x01])) #on
  device.char_write_handle(0x001f, bytearray([0x43, 0x42, intensity])) #intensiy
 else:
  device.char_write_handle(0x001f, bytearray([0x43, 0x40, 0x02])) #off

 return "OK"

if __name__ == "__main__":
 app.run(host='0.0.0.0',debug=True)
