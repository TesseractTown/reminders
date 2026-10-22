import PySimpleGUI as sg

sg.set_options(font=('assets/Jaini-Regular', 20))

class Popup():

    def __init__(self):
        pass

    def first_popup():

        sg.popup_no_buttons("","Take your meds!!","", auto_close= True, auto_close_duration=5, location= (2240, 624))

        if sg.popup_yes_no("Have you taken your meds?", keep_on_top=True, location= (2240, 624)) == 'Yes':
            exit()




# Needs to open another window after that window closes
