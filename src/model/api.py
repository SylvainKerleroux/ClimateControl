import time
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class API():
    
    API_KEY = "2f51ca9ab60128f4c2c3c8c6bc2be464"
    LOCATION = "Kingston, JM"

    def __init__(self):
        import pyowm
        self.owm = pyowm.OWM(self.API_KEY)
        log_file = logging.FileHandler('api_db.csv')
        log_file.setLevel(logging.DEBUG)
        logger.addHandler(log_file)

    def update(self, interval=3600, unit='celsius'):
        observation = self.owm.weather_at_place(self.LOCATION)
        while True:
            current = observation.get_weather()
            now = time.asctime(time.localtime(time.time()))
            res = "{location}, {time}, {temp}, {humid}".format(location=self.LOCATION,
                                                               time=now,
                                                               temp=current.get_temperature(unit)['temp'],
                                                               humid=current.get_humidity())
            logger.warning(res)
            time.sleep(interval)


if __name__ == "__main__":
    api = API()
    api.update(1)
