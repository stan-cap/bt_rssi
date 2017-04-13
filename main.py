from bt_proximity import BluetoothRSSI
import time
import sys
import datetime


#////////////////////////////////
BT_ADDR = 'C8:A8:23:EE:14:61'#/// Enter your bluetooth address here!
#////////////////////////////////


# ----------------------- DO NOT EDIT ANYTHING BELOW THIS LINE --------------------------- #




def write(records, count):
    f = open("records.txt", "a+") #open records for append. If not present create
    for i in range(count): #write out each record
        f.write(str(records[i][0]) + "," + str(records[i][1]) + '\n')
    f.close()

def time_diff(start_time):
    current_time = datetime.datetime.now()
    diff = (current_time - start_time).total_seconds()
    return str(diff)

def main(start_time):

    records = []
    count = 0
    addr = BT_ADDR
    num = 10

    while(count < num):      
        btrssi = BluetoothRSSI(addr=addr)
        current_time = time_diff(start_time)
        record = (btrssi.get_rssi(), current_time)
        records.append(record)
        count += 1
        time.sleep(.5)
    write(records, count)

if __name__ == '__main__':
    main()
