from bt_proximity import BluetoothRSSI
import time
import sys
import datetime


#////////////////////////////////
BT_ADDR1 = 'C8:A8:23:EE:14:61'#/// Enter your first bluetooth address here!
#////////////////////////////////

#////////////////////////////////
BT_ADDR2 = '00:CD:FE:9C:77:FD'#/// Enter your second bluetooth address here!
#////////////////////////////////

# ----------------------- DO NOT EDIT ANYTHING BELOW THIS LINE --------------------------- #




def write(records1, records2, count):
    f = open("records.txt", "a+")                      # open records for append. If not present create
    for i in range(count):                             # write out each record
        f.write(str(records1[i][0]) + "," + str(records1[i][1]) + '\n')
        f.write(str(records2[i][0]) + "," + str(records2[i][1]) + '\n')
    f.close()

def time_diff(start_time):
    current_time = datetime.datetime.now()             # get current time
    diff = (current_time - start_time).total_seconds() # get difference of startime and current time
    return str(diff)

def main(start_time):

    records1 = []                                       # initialize array of records
    records2 = []
    count = 0                                          # initialize count
    addr1 = BT_ADDR1                                     # assign BT_ADDR
    addr2 = BT_ADDR2
    num = 10                                           # amount of records to be recorded

    while(count < num):      
        btrssi1 = BluetoothRSSI(addr=addr1)
        btrssi2 = BluetoothRSSI(addr=addr2)
        time_e = time_diff(start_time)                 # get seconds elapsed
        record1 = (btrssi1.get_rssi(), time_e)           # create record
        record2 = (btrssi2.get_rssi(), time_e)
        records1.append(record1)                         # add record to records array
        records2.append(record2)
        count += 1
        time.sleep(.5)                                 # wait time to get next record
    write(records1, records2, count)                              # write out records

if __name__ == '__main__':
    main()
