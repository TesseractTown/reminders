import time
import PySimpleGUI as sg


class Stopwatch():

    def start_stopwatch(time_sec):

       while time_sec:
            mins, secs = divmod(time_sec, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            time_sec -= 1

    #def start_stopwatch():
        #Stopwatch.start_stopwatch()
