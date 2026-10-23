import time
from datetime import datetime
import PySimpleGUI as sg
from window_popup import Popup


class Stopwatch():

    def alarm():

        alarm_time = "22:40:00"

        while True:
            #print("inside loop")
            now = datetime.now().strftime("%H:%M:%S")
            #print(now)
            if now == alarm_time:
                print("inside if statement")
                Popup.first_popup()
                break
            time.sleep(1)

