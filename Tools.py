#Retrieve the required libraries 
import os
import platform

#Creating tasks, for example 
def open_notepad():
    os.system("notepad")

def open_calculator():
    os.system("calc")

def get_system_info():
    return platform.system() + " " + platform.release()

def list_files():
    return os.listdir()
