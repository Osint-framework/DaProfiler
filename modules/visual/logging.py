from datetime import datetime
import time

def terminal_loggin(log,text):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    text = (current_time, text)
    if log == "True":
        for i in text: 
            print(i, end ='', flush = True) 
            time.sleep(0.01)
