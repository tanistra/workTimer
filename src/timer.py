import datetime
import time

class Timer():

    def timer(self):
        data_print = datetime.datetime.now()
        data_formatted = str(data_print.strftime('%H:%M:%S'))
        return data_formatted

    def time_to_break(self, time_break):
        x = datetime.timedelta(seconds=time_break)
        return x

if __name__=='__main__':
    t = Timer()
    time1 = 30
    for i in range(0, time1):
        time1 -= 1
        t.time_to_break(time1)
        time.sleep(1)