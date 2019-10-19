#! /usr/local/bin/python

from datetime import datetime as dtm, timedelta
import time
import sys

class Pomodoro():

    def __init__(self, run_time):
        self.run_time = run_time
        self._initial_time = dtm.now()
        self.pomodoro_start = dtm.now()
        self.pomodoro_end = self.pomodoro_start + timedelta(minutes=self.run_time)
        self.checkmarks = 0
        self.breaks = 0
        self.break_start_time = None
        self.break_end_time = None
        self._end_time = None

    def _get_initial_time(self):
        return self._initial_time

    def get_pomodoro_start(self):
        return self.pomodoro_start

    def get_pomodoro_end(self):
        return self.pomodoro_end

    def start_pomodoro(self):
        self.pomodoro_start = dtm.now()
        self._set_pomodoro_end()
        return self.pomodoro_start

    def _set_pomodoro_end(self):
        self.pomodoro_end = self.pomodoro_start + timedelta(minutes=self.run_time)
        return self.pomodoro_end

    def remaining_pomodoro_time(self):
        return self.pomodoro_end - dtm.now()
        
    def all_done(self):
        return self.breaks == 4

    def start_break(self):
        print('Starting break')
        self.checkmarks += 1
        self.breaks += 1 
        self.break_start_time = dtm.now()
        self.which_break()
        return self.break_start_time
    
    def which_break(self):
        if self.breaks % 4 == 0:
            return self._big_break_time()
        return self._small_break_time()
    
    def _small_break_time(self):
        break_run_time = self.run_time * .15
        self.break_end_time = self.break_start_time + timedelta(minutes=break_run_time)
        return self.break_end_time

    def _big_break_time(self):
        break_run_time = self.run_time * .75
        self.break_end_time = self.break_start_time + timedelta(minutes=break_run_time)
        return self.break_end_time

    def get_break_end(self):
        return self.break_end_time

    def remaining_break_time(self):
        remainder = self.break_end_time - dtm.now()
        return remainder

if __name__ == "__main__":
    user_time = sys.argv[1]
    clean_user_time = int(user_time)
    pom = Pomodoro(clean_user_time)
    
    while True:
        print("Start next Pomodoro?")
        user_input = input()
        usr_input = user_input.lower()
        
        if usr_input in ['n', 'no']:
            print("Not the right time for a Pomodoro.")
            break 

        if usr_input in ['y', 'yes']:
            pom.start_pomodoro()
            time_remaining = pom.remaining_pomodoro_time()
            print(f"Starting a Pomodoro of {pom.run_time} minutes")
            print(f"The time now is {pom.pomodoro_start}, and you have until {pom.pomodoro_end}. This is the total of {time_remaining} seconds.")
            
            while True:
                time_remaining = pom.remaining_pomodoro_time()
                print(f"The time remaining is {time_remaining}")
                time.sleep(5) 
                if time_remaining <= timedelta(0, 5, 0):
                    break

            pom.start_break()
            print("Starting break")  
            print(f"The number of checkmarks is {pom.checkmarks} and the number of breaks is {pom.breaks}")
            while True:
                break_time_remaining = pom.remaining_break_time()
                print(f"The break time remaining is {break_time_remaining}")        
                time.sleep(5) 
                if break_time_remaining <= timedelta(0, 5, 0):
                    break

        if pom.all_done() == True:
            break