import time

class API():
    
    API_KEY = "2f51ca9ab60128f4c2c3c8c6bc2be464"
    LOCATION = "Kingston, JM"

    def __init__(self):
        import pyowm
        self.owm = pyowm.OWM(self.API_KEY)
    
    def run(self, interval=3600, unit='celsius'):
        observation = self.owm.weather_at_place(self.LOCATION)
        while True:
            current = observation.get_weather()
            now = time.asctime(time.localtime(time.time()))
            dic = {self.LOCATION : [now, current.get_temperature(unit)['temp'], current.get_humidity()]}
            yield dic
            time.sleep(interval)

if __name__ == "__main__":
    api = API()
    for output in api.run(10, 'fahrenheit'):
        print(output)
