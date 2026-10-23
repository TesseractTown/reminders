import time
from datetime import datetime
import PySimpleGUI as sg
from window_popup import Popup


class Stopwatch():

    def __init__(self, popup):
            self.popup = popup

    def alarm(self):

        alarm_time = "17:00:00"

        while True:
            now = datetime.now().strftime("%H:%M:%S")
            if now == alarm_time:
                self.popup.first_popup()
                break
            time.sleep(1)

