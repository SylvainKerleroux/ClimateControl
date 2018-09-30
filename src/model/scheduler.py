import api, sensors
from multiprocessing import Process

from datetime import date
from apscheduler.scheduler import Scheduler

# Start the scheduler
sched = Scheduler()
sched.start()

# Define the function that is to be executed
def my_job(text):
    print text

# The job will be executed on November 6th, 2009
exec_date = date(2009, 11, 6)

# Store the job in a variable in case we want to cancel it
job = sched.add_date_job(my_job, exec_date, ['text'])

def main():
    _api = api.API_Loop()
    _temp_humid = sensors.temp_humid

    Process(target=_api.run).start()
    Process(target=_temp_humid.run).start()

main()

