import PySimpleGUI as sg
import sys, os

class Popup():
    _relative_icon_path = "assets/icon.ico"

    def __init__(self):
        self.icon_path = os.path.abspath(self._relative_icon_path)
        sg.set_options(font=('assets/Jaini-Regular', 20))
        sg.theme('Purple')

    def first_popup(self):

        sg.popup_no_buttons("", "Take your meds!!", "", 
                            auto_close= True, 
                            auto_close_duration=120, 
                            location= (2240, 624), 
                            icon= self.icon_path, 
                            keep_on_top= True)

        yes_no_popup = sg.popup_yes_no("Have you taken your meds?", 
                                        keep_on_top=True, 
                                        location= (2150, 624),
                                        icon= self.icon_path)

        if yes_no_popup == 'Yes':
            pass
        else:
            sg.popup_no_buttons(
                "", "Take your meds!!", "", 
                auto_close= True, 
                auto_close_duration=120, 
                location= (2240, 624),
                icon= self.icon_path)
    
