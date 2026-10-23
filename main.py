from window_popup import Popup
from stopwatch import Stopwatch


if __name__ == '__main__':
    
    popup = Popup()
    #popup.first_popup() #only used for testing GUI

    stopwatch = Stopwatch(popup)
    control = True

    while control == True:
        stopwatch.alarm()
