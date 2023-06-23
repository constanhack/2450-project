from data_model import DataModel
from control_ops_v2 import Halt

def Read(act_nums,mem,window):
    #Read a word from the keyboard into a specific location in memory.
    while True:
        window.appendOutput(f"Please enter a word: (Type 'q' to exit)")
        word = input("Please enter a word: (Type 'q' to exit) ")
        if word in ['Q','q']:
            return Halt(mem)
        if mem.validate_value(word):
            break

        
    mem.set_mem_value(int(word),act_nums)
    return True

def Write(act_nums,mem,window):
    #Write a word from a specific location in memory to screen.
    word = mem.get_mem_value(act_nums)
    if mem.validate_value(word):
        window.appendOutput(str(word))
        return True
    return Halt(mem)