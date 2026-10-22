import PySimpleGUI as sg
import sys, os

sg.set_options(font=('assets/Jaini-Regular', 20))
sg.theme('Purple')


def resource(relative_path):
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Popup():

    def __init__(self):
        pass

    def first_popup():

        sg.popup_no_buttons("","Take your meds!!","", auto_close= True, 
                            auto_close_duration=120, 
                            location= (2240, 624), 
                            icon= resource("assets/windowicon.ico"), 
                            keep_on_top= True)

        if sg.popup_yes_no("Have you taken your meds?", keep_on_top=True, 
                           location= (2150, 624),
                           icon= resource("assets/windowicon.ico")) == 'Yes':
            pass
        else:
            sg.popup_no_buttons("","Take your meds!!","", auto_close= True, auto_close_duration=120, location= (2240, 624))
    
