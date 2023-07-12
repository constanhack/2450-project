from data_model import DataModel
from control_ops_v2 import Halt
import time

from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QPushButton

class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.input_text = QLineEdit()
        self.confirm_button = QPushButton('Enter')
        self.confirm_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        inputText = self.input_text
        inputText.setStyleSheet('background-color: white;')
        layout.addWidget(inputText)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)

    def get_input(self):
        return self.input_text.text()

def Read(act_nums, mem, window):
    # Create an instance of the input dialog
    dialog = InputDialog(window)
    dialog.setModal(True)

    # Show the dialog and wait for user input
    if dialog.exec() == QDialog.DialogCode.Accepted:
        user_input = dialog.get_input()
        # Process the user input as needed
        if user_input == 'q':
            exit()

        invalid_msg = "Invalid Character entered. Enter 'q' to exit or try again."

        if len(user_input) == 5:
            if user_input[0] not in ('+', '-'):
                window.appendOutput(invalid_msg)
                Read(act_nums, mem, window)
            if user_input[1] not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                window.appendOutput(invalid_msg)
                Read(act_nums, mem, window)
            if user_input[2] not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                window.appendOutput(invalid_msg)
                Read(act_nums, mem, window)
            if user_input[3] not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                window.appendOutput(invalid_msg)
                Read(act_nums, mem, window)
            if user_input[4] not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                window.appendOutput(invalid_msg)
                Read(act_nums, mem, window)
                
        elif len(user_input) == 4:
            '''for char in user_input:
                if char not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                    window.appendOutput("Invalid Character entered")
                    exit()'''
            if user_input[0] not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                window.appendOutput(invalid_msg)
                Read(act_nums, mem, window)
            if user_input[1] not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                window.appendOutput(invalid_msg)
                Read(act_nums, mem, window)
            if user_input[2] not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                window.appendOutput(invalid_msg)
                Read(act_nums, mem, window)
            if user_input[3] not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                window.appendOutput(invalid_msg)
                Read(act_nums, mem, window)
                
        else:
            window.appendOutput("Error, characters must be 4 digits. Enter 'q' to exit or try again.")
            Read(act_nums, mem, window)
        
        '''try:
            if len(user_input) > 5:
                window.appendOutput("Invalid Character entered")
            if len(user_input) == 5:
                if user_input[0] not in ('+', '-'):
                    window.appendOutput("Invalid Character entered")
                for val in user_input[1:5]:
                    int(val)
            if len(user_input) < 5:
                try:
                    for val in user_input[1:5]:
                        int(val)
                except ValueError:
                    window.appendOutput("Error, characters must be digits")
                    #print("Error, characters must be digits")
                    exit()
        
        except ValueError:
            window.appendOutput("Error, last 4 characters must be digits")
            #print("Error, last 4 characters must be digits")
            exit()'''
        
        if int(user_input) >= 0:
            window.appendOutput(f'Input of {user_input} has been read into mem location {act_nums}')
        else:
            window.appendOutput(f'Input of {user_input} has been read into mem location {act_nums}')
        mem.set_mem_value(int(user_input),act_nums)  

def Write(act_nums,mem,window):
    #Write a word from a specific location in memory to screen.
    word = mem.get_mem_value(act_nums)
    if mem.validate_value(word):
        window.appendOutput(str(word))
        return True
    return Halt(mem)