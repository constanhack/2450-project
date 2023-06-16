import tkinter as tk
from tkinter import filedialog

def Allocate_Memory(file,memory_size):
    MEM = dict()
    for i in range(memory_size):
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
    return open(file_path,'r')



