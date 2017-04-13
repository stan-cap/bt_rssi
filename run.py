import main
import datetime
import time

f = open("records.txt", "a+")        # open text file for editting
f.write("RSSI, sec_elapsed" + '\n')  # add headers to text file
f.close()

time.sleep(10)                       # sleep for 10 seconds to allow Bluetooth Services to start

start_time = datetime.datetime.now() # get relative start time
exec_count = 0                       # initialize counter
exec_amt = 12000                     # amount of times to execute main which records 10 records

while (exec_count < exec_amt):       # execute main.py while count is less than amount
    main.main(start_time)
    exec_count += 1
