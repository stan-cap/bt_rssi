import main
import datetime

start_time = datetime.datetime.now()
exec_count = 0
exec_amt = 2

while (exec_count < exec_amt):
    main.main(start_time)
    exec_count += 1
