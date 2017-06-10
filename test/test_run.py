import test_main
import datetime
import time

f = open("test_records.txt", "w")    # open text file for editting
f.write("RSSI, sec_elapsed" + '\n')  # add headers to text file
f.close()

start_time = datetime.datetime.now() # get relative start time
exec_count = 0                       # initialize counter
exec_amt = 2                         # amount of times to execute main.py which records 10 records

while (exec_count < exec_amt):       # execute main.py while count is less than amount
    test_main.main(start_time)
    exec_count += 1
