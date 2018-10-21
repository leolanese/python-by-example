# Python job scheduling for humans.
# An in-process scheduler for periodic jobs that uses the builder pattern for configuration. 
# Schedule lets you run Python functions (or any other callable) periodically at pre-determined intervals using a simple, 
# human-friendly syntax.

# pip install schedule
# https://schedule.readthedocs.io/en/stable

###########################################################################

import schedule
import time

# execute a job in serie
def job():
    print("I'm working... 1 minute passed!!")

# jobs triggers
schedule.every(1).minutes.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

# job loops
while True:
    schedule.run_pending()
    time.sleep(1)

##########################################################################

# execute jobs in parallel
import threading
import time
import schedule

def job():
    print("I'm running on thread %s" % threading.current_thread())

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

schedule.every(10).seconds.do(run_threaded, job)
schedule.every(10).seconds.do(run_threaded, job)
schedule.every(10).seconds.do(run_threaded, job)
schedule.every(10).seconds.do(run_threaded, job)
schedule.every(10).seconds.do(run_threaded, job)

while 1:
    schedule.run_pending()
    time.sleep(1)
    
    
