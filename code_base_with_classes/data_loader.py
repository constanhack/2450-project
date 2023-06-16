import tkinter as tk
from tkinter import filedialog

class DataLoader:
    def __init__(self,memory_size = 100):
        def File_Picker():
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename()
            if file_path == '':
                print('No selection made, closing program.')
                exit()    
            return file_path
        
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
        
        self._private_data_file_path = File_Picker()
        self._private_data_dictionary =  Allocate_Memory(open(self._private_data_file_path,'r'), memory_size)

    def get_data(self):
        return self._private_data_dictionary
    