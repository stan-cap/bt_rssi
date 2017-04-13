import main
import datetime
import time

time.sleep(10)

start_time = datetime.datetime.now()
exec_count = 0
exec_amt = 12000

while (exec_count < exec_amt):
    main.main(start_time)
    exec_count += 1
