import Adafruit_DHT as Ada
import time

class Sensor(object):
	def __init__(self, type, pin):
		self.sensor = type
		self.pin = pin

	def read(self):
		output = Ada.read_retry(self.sensor, self.pin)
		return output
        
        def run(self, interval=1, callback='print'):
            while True:
                res = self.read()
                if callback == 'print':
                    print(res)
                else: 
                    callback(res)
                time.sleep(interval)

temp_humid = Sensor(Ada.DHT22, 4)

if __name__ == "__main__":
	print(temp_humid.read())
