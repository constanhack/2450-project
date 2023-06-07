import tkinter as tk
from tkinter import filedialog

def Allocate_Memory(file):
    MEM = dict()
    for i in range(100):
        if i < 10:
            MEM[f'0{i}'] = '+0000'
        else:
            MEM[f'{i}'] = '+0000'    
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

def Get_Value(PC,MEM):
    if PC < 10:
        try:
            return MEM[f'0{PC}']
        except KeyError:
            print(f'Invalid location of 0{PC}.  Closing Program')
            exit()
    try:
        return MEM[f'{PC}']
    except KeyError:
            print(f'Invalid location of {PC}.  Closing Program')
            exit()
