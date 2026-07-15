import tkinter as tk
from tkinter import Tk
import sys
import subprocess


main_process = None  # Global variable to hold the main.py process

def run_main():
    global main_process
    if main_process is None or main_process.poll() is not None:  # Check if the process is not running
        main_process = subprocess.Popen([sys.executable, "main.py"])  # Start main.py in a new process
    else:
        print("main.py is already running.")
        subprocess.Popen([sys.executable, "main.py"]) # this opens my main file


def stop_main():
    global main_process
    if main_process and main_process.poll() is None:
        main_process.terminate()
        main_process.wait()
        main_process = None


window = tk.Tk()
window.title("Wifi Cracker")
window.geometry("400x400")


#widgit
button = tk.Button(window, text="Start Cracking", command=run_main) 

button2 = tk.Button(window, text="Stop Cracking", command=stop_main)



#pack
button.pack()
button2.pack()



window.mainloop()