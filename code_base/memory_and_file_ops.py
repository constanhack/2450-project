import tkinter as tk
from tkinter import filedialog

def Allocate_Memory(file):
    mem = dict()
    index = 0
    for line in file:
        if index < 10:
            mem[f'0{index}'] = line.strip()
        else:
            mem[f'{index}'] = line.strip()
        index += 1
    return mem

def File_Picker():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if file_path == '':
        print('No selection made, closing program.')
        exit()    
    return file_path
