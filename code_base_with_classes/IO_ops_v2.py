from data_model import DataModel
from control_ops_v2 import Halt
import time

def Read(act_nums,mem,window):
    #Read a word from the keyboard into a specific location in memory.
    window.Enter.setEnabled(True)

    # How to wait for input to get added?
    # You can't even check for inputs if the program is asleep.
    # print("sleeping")
    # time.sleep(5) 
    # print("done sleeping")
    
    # validate the input 
    for x in window.InputText.text():
            if len(x) > 5:
                print("Invalid Character entered")
                return
            if x[0] not in ('+','-'):
                print("Error, word must begin with '-' or '+'")
                return
            try:
                int(x[1:5])
                return
            except ValueError:
                print("Error, last 4 characters must be digits")
                return

    # grab the input
    input = window.InputText.text() 
    print(input)

    # ERROR: while loops seem to crash. Trying to wait for Enter button to be pressed.
    # while window.Enter.isChecked() == False:
    #     if window.Enter.isChecked():
    #         print('Enter pressed')
    #         break
        
    # while True:
    #     window.appendOutput(f"Please enter a word: (Type 'q' to exit)")
    #     word = input("Please enter a word: (Type 'q' to exit) ")
    #     word = "none"
    #     word = window.getInput()
    #     if word in ['Q','q']:
    #         return Halt(mem)
    #     if mem.validate_value(word):
    #         break
    # mem.set_mem_value(int(word),act_nums)
    return True
        



def Write(act_nums,mem,window):
    #Write a word from a specific location in memory to screen.
    word = mem.get_mem_value(act_nums)
    if mem.validate_value(word):
        window.appendOutput(str(word))
        return True
    return Halt(mem)