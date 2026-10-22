import PySimpleGUI as sg
from stopwatch import Stopwatch

sg.set_options(font=('assets/Jaini-Regular', 20))

class Popup():

    def first_popup():

        sg.popup_no_buttons("","Take your meds!!","", auto_close= True, auto_close_duration=5, )

        if sg.popup_yes_no(keep_on_top=True) == 'Yes':
            exit()


# Needs to open another window after that window closes
