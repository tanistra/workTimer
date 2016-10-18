from tkinter import *
from src.timer import Timer
import time


class WorkTimer(Frame):
    interval = 0
    def __init__(self, master):
        super(WorkTimer, self).__init__(master)
        self.timer = Timer()

        self.clock_lbl = Label(text="",font=('times', 20, 'bold'), bg='green')
        self.clock_lbl.pack(fill=BOTH)
        self.last_break = Label(text="",font=('times', 20, 'bold'), bg='red')
        self.last_break.pack(fill=BOTH)
        self.next_break = Label(text="",font=('times', 20, 'bold'), bg='yellow')
        self.next_break.pack(fill=BOTH)

        self.update_clock()
        # self.update_time_to_break()
        self.set_interval_lbl = Label(root, text="Set break interval in minutes:")
        self.set_interval_entry = Entry(root)
        self.start_btn = Button(root,
                                text='Start Timer',
                                command=lambda: self.start_timer())
        self.quit_btn = Button(root,
                            text="Quit",
                            command=root.quit)
        self.set_widget()

    def set_widget(self):
        self.start_btn.place(x=200, y=250)
        self.start_btn.config(width=10, height=2)
        self.quit_btn.place(x=100, y=250)
        self.quit_btn.config(width=10, height=2)

        self.set_interval_lbl.place(y=130, anchor=W)
        self.set_interval_lbl.config(width=25, height=1)
        self.set_interval_entry.place(x=170,y=130, anchor=W)
        self.set_interval_entry.config(width=15)

    def update_clock(self):
        now = self.timer.timer()
        self.clock_lbl.configure(text=now)
        root.after(1000, self.update_clock)

    def get_interval(self):
        self.interval = int(self.set_interval_entry.get()) * 60
        return self.interval


    # def update_time_to_break(self):
    #     break_time = self.timer.time_to_break()
    #     self.next_break.configure(text=break_time)
    #     root.after(1000, self.update_time_to_break)

    def start_timer(self):
        try:
            self.interval = self.get_interval()
        except ValueError as e:
            self.interval = 0
        print(self.interval)
        self.next_break.configure(text=self.timer.time_to_break(self.interval))
        root.after(1000)

        # for i in range(interval):
        #     interval -= 1
        #     print(self.timer.time_to_break(interval))
        #     time.sleep(1)



root = Tk()
root.title("WorkTimer")
root.geometry("300x300")
app = WorkTimer(root)
app.pack()
root.mainloop()
