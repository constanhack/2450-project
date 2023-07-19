import tkinter as tk
from tkinter import filedialog

class DataLoader:
    def __init__(self, memory_size = 250, testing = False, testing_file_path = ''):
        def File_Picker():
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename()  
            return file_path
        
        def Allocate_Memory(file,memory_size):
            MEM = dict()
            for i in range(memory_size):
                if i < 10:
                    MEM[f'00{i}'] = '+000000'
                elif i < 100:
                    MEM[f'0{i}'] = '+000000'
                else:
                    MEM[f'{i}'] = '+000000'    
            index = 0
            for line in file:
                if index < 10:
                    MEM[f'00{index}'] = line.strip()
                elif index < 100:
                    MEM[f'0{index}'] = line.strip()
                else:
                    MEM[f'{index}'] = line.strip()
                index += 1
            return MEM
        
        self._private_data_file_path = testing_file_path if testing == True else File_Picker()
        self._private_data_dictionary =  Allocate_Memory(open(self._private_data_file_path,'r'), memory_size) if self._private_data_file_path else ''

    def get_data(self):
        return self._private_data_dictionary
    
    def get_file_path(self):
        return self._private_data_file_path
    