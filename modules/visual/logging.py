import time

def terminal_loggin(log,text):
    if log == "True":
        for i in text: 
            print(i, end ='', flush = True) 
            time.sleep(0.01) 