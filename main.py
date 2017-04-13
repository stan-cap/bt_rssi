from bt_proximity import BluetoothRSSI
import time
import sys
import datetime


#////////////////////////////////
BT_ADDR = 'C8:A8:23:EE:14:61'#/// Enter your bluetooth address here!
#////////////////////////////////


# ----------------------- DO NOT EDIT ANYTHING BELOW THIS LINE --------------------------- #




def write(records, count):
    f = open("records.txt", "a+")                      # open records for append. If not present create
    for i in range(count):                             # write out each record
        f.write(str(records[i][0]) + "," + str(records[i][1]) + '\n')
    f.close()

def time_diff(start_time):
    current_time = datetime.datetime.now()             # get current time
    diff = (current_time - start_time).total_seconds() # get difference of startime and current time
    return str(diff)

def main(start_time):

    records = []                                       # initialize array of records
    count = 0                                          # initialize count
    addr = BT_ADDR                                     # assign BT_ADDR
    num = 10                                           # amount of records to be recorded

    while(count < num):      
        btrssi = BluetoothRSSI(addr=addr)
        time_e = time_diff(start_time)                 # get seconds elapsed
        record = (btrssi.get_rssi(), time_e)           # create record
        records.append(record)                         # add record to records array
        count += 1
        time.sleep(.5)                                 # wait time to get next record
    write(records, count)                              # write out records

if __name__ == '__main__':
    main()
