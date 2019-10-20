#! /usr/local/bin/python
import argparse
from datetime import datetime as dtm, timedelta
import time
import sys


class Pomodoro:
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

    def _get_final_run_time(self):
        return dtm.now() - self._get_initial_time()

    def focus_report(self):
        print(
            f"\nThe user made it through:\n"
            f"- {self.checkmarks} Pomodoro(s)\n"
            f"- {self.breaks} break(s) \n\n"
            f"The user had a focus time of:\n"
            f"- {self._get_final_run_time()} minutes"
        )

    def _get_pomodoro_start(self):
        return self.pomodoro_start

    def _get_pomodoro_end(self):
        return self.pomodoro_end

    def start_pomodoro(self):
        print(f"Starting a Pomodoro of {self.run_time} minutes.")
        self._start_pomodoro()
        self._run_pom_countdown()

    def _start_pomodoro(self):
        self.pomodoro_start = dtm.now()
        self._set_pomodoro_end()
        return self.pomodoro_start

    def _set_pomodoro_end(self):
        self.pomodoro_end = self.pomodoro_start + timedelta(minutes=self.run_time)
        return self.pomodoro_end

    def remaining_pomodoro_time(self):
        time_remaining = self.pomodoro_end - dtm.now()
        return time_remaining

    def all_done(self):
        return self.breaks == 4

    def start_break(self):
        print("Starting break")
        self.checkmarks += 1
        print(f"You have {self.checkmarks} checkmarks.")
        break_duration = self._set_break_duration_by_checkmarks()
        print(f"running a break for {break_duration}")
        self._run_break_countdown()
        self.breaks += 1
        print(f"You have taken {self.breaks} breaks")

    def _set_break_start_time(self):
        self.break_start_time = dtm.now()
        return self.break_start_time

    def _set_break_duration_by_checkmarks(self):
        self._set_break_start_time()
        if self.checkmarks % 4 == 0:
            return self._set_break_duration(0.75)
        return self._set_break_duration(0.15)

    def _set_break_duration(self, run_time=None):
        run_time = self.run_time * run_time
        self.break_end_time = self.break_start_time + timedelta(minutes=run_time)
        return self.break_end_time

    def get_break_end(self):
        return self.break_end_time

    def remaining_break_time(self):
        remainder = self.break_end_time - dtm.now()
        return remainder

    def _run_pom_countdown(self):
        while True:
            time_remaining = self.remaining_pomodoro_time()
            print(
                f"Keep your focus. You have {time_remaining} remaining in this Pomodoro.\n"
            )
            time.sleep(5)
            if time_remaining <= timedelta(0, 5, 0):
                break

    def _run_break_countdown(self):
        while True:
            break_time_remaining = self.remaining_break_time()
            print(
                f"Whew!! Take a break. You have {break_time_remaining} left in your break\n"
            )
            time.sleep(5)
            if break_time_remaining <= timedelta(0, 5, 0):
                break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="POMODORO")
    parser.add_argument("-m", "--min", help="set run time in minutes", dest="min")
    args = parser.parse_args()
    user_time = args.min

    clean_user_time = int(user_time)
    pom = Pomodoro(clean_user_time)

    try:
        while True:
            print("Start next Pomodoro? [Y/N]")
            user_input = input()
            usr_input = user_input.lower()

            if usr_input in ["n", "no"]:
                print("Not the right time for a Pomodoro.")
                break

            if usr_input in ["y", "yes"]:
                pom.start_pomodoro()
                pom.start_break()

            if pom.all_done() == True:
                break

    except KeyboardInterrupt:
        pass

    finally:
        pom.focus_report()
