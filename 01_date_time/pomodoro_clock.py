from datetime import datetime as dtm, timedelta
import time
import sys

class Pomodoro():
    def __init__(self, run_time, start_again=False):
        self.run_time = run_time
        self._initial_time = dtm.now()
        self.number_of_check_marks = 0
        self.number_of_breaks = 0
        self.pomodoro_time = self._initial_time + timedelta(minutes=self.run_time)
        self.start_again = False
        self.remaining_time = self.pomodoro_time - self._initial_time
        self.small_break = 0
        self.big_break = 0

    def _get_initial_time(self):
        return self._initial_time

    def _small_break(self):
        q, r = divmod(self.pomodoro_time, .15)
        return r

    def _big_break(self):
        q, r = divmod(self.pomodoro_time, .75)
        return r

    def all_done(self):
        return self.number_of_breaks == 4 and self.number_of_check_marks == 4

    def _get_rest_time(self):
        if self.number_of_checks == 4:
            break_duration = _big_break()
            return "You have completed 4 pomodoros. Take a {break_duration} minute break.".format(break_duation)
        break_duration = _small_break() 
        return "Take a {break_duration} minute break".format(break_duration)

    def _get_time(self):
        return self.pomodoro_time
   

    def _remaining_time(self):
        self.remaining_time = self.pomodoro_time - dtm.now()
        return self.remaining_time

    def get_user_check(self):
        pass    

    def _break(self):
        self.number_of_check_marks += 1
        self._get_rest_time()


if __name__ == "__main__":
    user_time = sys.argv[1]
     

    while True:
        print("Start next Pomodoro?")
        user_input = input()
        if user_input.lower() in ['y', 'yes']:
            clean_user_time = int(user_time)
            print(f"Starting a Pomodoro of {user_time} minutes")
            pom = Pomodoro(clean_user_time)
            start = pom._get_initial_time()
            end = pom._get_time()
            sec_rem = pom._remaining_time()
            print(f"The time now is {start}, and you have until {end}. This is the total of {sec_rem} seconds.")
            
            while True:
                time_remaining = pom._remaining_time()
                print(f"The time remaining is {time_remaining}")
                time.sleep(5) 
                if time_remaining <= timedelta(0, 5, 0):
                    break

        if pom.all_done() == True:
            break

            
            

        
