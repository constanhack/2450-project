from config import MEM, ACC, PC
import tkinter as tk
from tkinter import filedialog

def Allocate_Memory(file):
    ##mem = dict()
    index = 0
    for line in file:
        if index < 10:
            MEM[f'0{index}'] = line.strip()
        else:
            MEM[f'{index}'] = line.strip()
        index += 1
    return MEM

def File_Picker():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if file_path == '':
        print('No selection made, closing program.')
        exit()    
    return file_path

def Get_Value(PC):
    if PC < 10:
        return MEM[f'0{PC}']
    return MEM[f'{PC}']
