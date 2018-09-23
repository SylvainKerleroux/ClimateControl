import api, sensors
from multiprocessing import Process

def main():
    _api = api.API_Loop()
    _temp_humid = sensors.temp_humid

    Process(target=_api.run).start()
    Process(target=_temp_humid.run).start()

main()

