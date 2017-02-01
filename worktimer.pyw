from tkinter import *
from src.timer import Timer
from tkinter import messagebox
import winsound
import os


class WorkTimer(Frame):
    interval_val = -1
    start_interval_val = 0
    last_break_val = 0
    breaks = 0

    def __init__(self, master):
        super(WorkTimer, self).__init__(master)
        self.timer = Timer()

        self.clock_lbl = Label(text="", font=('times', 20, 'bold'), bg='green')
        self.clock_lbl.pack(fill=BOTH)
        self.last_break = Label(text="", font=('times', 20, 'bold'), bg='red')
        self.last_break.pack(fill=BOTH)
        self.next_break = Label(text="", font=('times', 20, 'bold'), bg='yellow')
        self.next_break.pack(fill=BOTH)
        self.breaks_counter = (Label(text="", font=('times', 20, 'bold'), bg='blue'))
        self.breaks_counter.pack(fill=BOTH)

        self.set_interval_lbl = Label(root, text="Set break interval in minutes:")
        self.set_interval_entry = Entry(root)
        self.start_btn = Button(root,
                                text='Start Timer',
                                command=self.start_timer)
        self.quit_btn = Button(root,
                               text="Quit",
                               command=root.quit)
        self.update_clock()
        self.update_time_to_break()
        self.update_last_break()
        self.update_breaks_counter()
        self.loop_interval()
        self.set_widget()

    def set_widget(self):
        self.start_btn.place(x=200, y=250)
        self.start_btn.config(width=10, height=2)
        self.quit_btn.place(x=100, y=250)
        self.quit_btn.config(width=10, height=2)

        self.set_interval_lbl.place(y=170, anchor=W)
        self.set_interval_lbl.config(width=25, height=1)
        self.set_interval_entry.place(x=170, y=170, anchor=W)
        self.set_interval_entry.config(width=15)

    def update_clock(self):
        now = self.timer.timer()
        self.clock_lbl.configure(text=now)
        root.after(1000, self.update_clock)

    def get_interval(self):
        try:
            self.interval_val = int(self.set_interval_entry.get()) * 60
        except ValueError:
            return self.interval_val
        return self.interval_val

    def loop_interval(self):
        if self.interval_val < 1:
            self.interval_val = self.get_interval()

    def update_time_to_break(self):
        if self.interval_val % 600 == 0:
            soundfile = os.path.join(os.path.dirname(__file__), "Alarm04.wav")
            winsound.PlaySound(soundfile, winsound.SND_FILENAME | winsound.SND_ASYNC)
        if self.interval_val > 0:
            break_time = self.timer.time_to_break(self.interval_val)
            self.interval_val -= 1
            self.next_break.configure(text=break_time)
        elif self.interval_val == 0:
            self.time_to_coffe()
            self.breaks += 1
            self.update_breaks_counter()
            self.interval_val = self.start_interval_val
            self.last_break_val = self.timer.timer()
        root.after(1000, self.update_time_to_break)

    def time_to_coffe(self):
        soundfile = os.path.join(os.path.dirname(__file__), "clock-cuckoo.wav")
        winsound.PlaySound(soundfile, winsound.SND_FILENAME | winsound.SND_ASYNC)
        messagebox.showinfo("Break time", "Move your ass!!\nLet's take break for few minutes")

    def update_last_break(self):
        last = self.last_break_val
        if last != 0:
            self.last_break.configure(text=last)
        root.after(1000, self.update_last_break)

    def update_breaks_counter(self):
        self.breaks_counter.configure(text=self.breaks)

    def start_timer(self):
        self.interval_val = self.get_interval()
        self.start_interval_val = self.interval_val


root = Tk()
root.title("WorkTimer")
root.geometry("300x300")
app = WorkTimer(root)
app.pack()
root.mainloop()
