import sys
import time
from PyQt6 import QtWidgets, uic
from data_loader import DataLoader
from data_model import DataModel
from driver import main
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLineEdit, QApplication, QDialog, QVBoxLayout, QPushButton, QLabel, QTableWidget, QTableWidgetItem
from UVSim import Ui_MainWindow 
from PyQt6 .QtGui import QColor
import tkinter as tk
from tkinter import filedialog
from random import randint

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    open_windows = []  # List to store references to all open AnotherWindow instances
    window_count = 1
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.ChooseFile.clicked.connect(self.chooseFileButtonClicked)
        self.Clear.clicked.connect(self.clearFilePath)
        self.Start.clicked.connect(self.submitFilePath)
        self.ColorSelect.clicked.connect(self.colorBox)
        self.NewTab.clicked.connect(self.addNewWindow)
        self.setWindowTitle(f"Window {MainWindow.window_count}")

    def addNewWindow(self):
        new_window = MainWindow()
        new_window.show()
        self.open_windows.append(new_window)
        MainWindow.window_count += 1
        new_window.setWindowTitle(f"Window {MainWindow.window_count}")

    def chooseFileButtonClicked(self):
        self.OutputText.clear()
        self._data = DataLoader()
        self.FilePath.setText(self._data.get_file_path())

    def clearFilePath(self):
        self.OutputText.clear()
        self.FilePath.clear()

    def submitFilePath(self):
        self.OutputText.clear()
        filepath = self.FilePath.text()
        if filepath:
            editWindow = FileEditBox(self)
            editWindow.setModal(True)
            if editWindow.exec() == QDialog.DialogCode.Accepted:
                main(DataModel(self._data), self)
                self.FilePath.clear()
                self.appendOutput('Program Complete\nSelect a file to run again')
        else:
            self.OutputText.setText('Please Select A File To start')
    
    def enterClicked(self):
        self.Enter.setChecked(True)
        user_input = self.getInput()
        return user_input

    def displayOutput(self,value):
        self.OutputText.clear()
        self.OutputText.setText(value)

    def appendOutput(self,value):
        self.OutputText.append(value)

    def getInput(self):
        input = self.InputText.text()
        return input

    def colorBox(self):
        """Allows the user to enter a color."""
        dialog = ColorInputBox(self)
        dialog.setModal(True)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            user_input1, user_input2 = dialog.get_inputs()

            # Validate color format
            if isValidHex(user_input1) and isValidHex(user_input2):
                # Attempt to set the main window background color
                self.setStyleSheet(f"background-color: #{user_input1};")
                # Attempt to set button and label colors
                color2_button = f"QPushButton{{background-color: #{user_input2};}}"
                color2_label = f"color: #{user_input2};"
                self.ChooseFile.setStyleSheet(color2_button)
                self.Clear.setStyleSheet(color2_button)
                self.Start.setStyleSheet(color2_button)
                self.ColorSelect.setStyleSheet(color2_button)
                self.Title.setStyleSheet(color2_label)
                self.Output.setStyleSheet(color2_label)
                self.Desc1.setStyleSheet(color2_label)
                self.Desc2.setStyleSheet(color2_label)
                self.label.setStyleSheet(color2_label)
            else:
                self.appendOutput("Invalid hexidecimal number.")

def isValidHex(color):
    try:
        if len(color) == 6:
            int(color, 16)
            return True
        return False
    except ValueError:
        return False

class TableWidget(QTableWidget):
    def __init__(self, rows, columns, parent=None):
        super().__init__(rows, columns)
    
    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if event.key() == Qt.Key.Key_V and (event.modifiers() & Qt.KeyboardModifier.ControlModifier):
            selection = self.selectedIndexes()

            if selection:
                row_anchor = selection[0].row()
                column_anchor = selection[0].column()

                clipboard = QApplication.clipboard()

                rows = clipboard.text().split('\n')
                for indx_row, row in enumerate(rows):
                    values = row.split('\t')
                    for indx_col, value in enumerate(values):
                        item = QTableWidgetItem(value)
                        item.setBackground(QColor(255,255,255))
                        self.setItem(row_anchor + indx_row, column_anchor + indx_col, item)

        if event.key() == Qt.Key.Key_C and (event.modifiers() & Qt.KeyboardModifier.ControlModifier):
            selection = sorted(self.selectedIndexes())

            copy_text = ''
            max_row, max_column = selection[-1].row(), selection[-1].column()

            for c in selection:
                copy_text += self.item(c.row(), c.column()).text()

                if c.row() == max_row and c.column() == max_column:
                    break

                if c.column() == max_column:
                    copy_text += '\n'
                else:
                    copy_text += '\t'

            QApplication.clipboard().setText(copy_text)

        if event.key() == Qt.Key.Key_X and (event.modifiers() & Qt.KeyboardModifier.ControlModifier):
            selection = sorted(self.selectedIndexes())

            copy_text = ''
            max_row, max_column = selection[-1].row(), selection[-1].column()

            for c in selection:
                copy_text += self.item(c.row(), c.column()).text()
                self.item(c.row(),c.column()).setText('')

                if c.row() == max_row and c.column() == max_column:
                    break

                if c.column() == max_column:
                    copy_text += '\n'
                else:
                    copy_text += '\t'

            QApplication.clipboard().setText(copy_text)

class FileEditBox(QDialog):
    def __init__(self, parent=None):
        self.parent = parent 
        super().__init__(parent)
        self.window_width, self.window_height = 200, 500
        self.setWindowTitle("Edit File")
        self.setMinimumSize(self.window_width, self.window_height)
        self.setStyleSheet('''
            QWidget {
                font-size: 12px;
            }
        ''')   

        self.layout = {}
        self.layout['main'] = QVBoxLayout()
        self.setLayout(self.layout['main'])

        self.table = TableWidget(250, 1,parent)
        self.table.setHorizontalHeaderLabels(['Values'])
        self.table.setSortingEnabled(False)
        
        values = [] if self.parent.checkBox.isChecked() == True else parent._data.get_data().values()
        if self.parent.checkBox.isChecked() == True:
            for item in parent._data.get_data().values():
                if len(item) == 5 and (item[0] == '+' or item[0] == '-'):
                    converted_item = item[0] + '0' + item[1:3] + '0' + item[3:5]
                    values.append(converted_item)
                else:
                    values.append(item)

        rowLabels = []
        i = 0           
        for item in values:
             rowLabels.append(str(i))
             tableWidget = QTableWidgetItem(str(item))
             tableWidget.setBackground(QColor(255,255,255))
             self.table.setItem(i,0,tableWidget)
             i += 1
        self.table.setVerticalHeaderLabels(rowLabels)
        self.layout['main'].addWidget(self.table)

        self.submit_button = QPushButton("Submit", self)
        self.submit_button.setStyleSheet("background-color: white;")
        self.submit_button.clicked.connect(self.handle_submit)
        self.layout['main'].addWidget(self.submit_button)

        self.save_button = QPushButton("Save", self)
        self.save_button.setStyleSheet("background-color: white;")
        self.save_button.clicked.connect(self.file_saver)
        self.layout['main'].addWidget(self.save_button)
        
    def handle_submit(self):
        rows = self.table.rowCount()
        columns = self.table.columnCount()

        mem = dict()
        
        for row in range(rows):
            for column in range(columns):
                item = self.table.item(row, column)
                if item is not None:
                    value = item.text()
                    if row < 10:
                        mem[f'00{row}'] = value if value != '' else '+000000'
                    elif row < 100:
                        mem[f'0{row}'] = value if value != '' else '+000000'
                    else:
                        mem[f'{row}']  = value if value != '' else '+000000'
        self.parent._data = mem
        self.close()
        self.accept()

    def file_saver(self):
        file = filedialog.asksaveasfilename(filetypes=[("txt file", ".txt")], defaultextension=".txt")
        if file == '':
            return
        rows = self.table.rowCount()
        columns = self.table.columnCount()

        file_data = []
        
        for row in range(rows):
            for column in range(columns):
                item = self.table.item(row, column)
                if item is not None:
                    value = item.text()
                    file_data.append(value) if value != '' else file_data.append('+000000')

        with open(file,'w') as write_file:
            write_file.write('\n'.join(file_data))

class ColorInputBox(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Change Color")

        self.instruction_label = QLabel("Please enter colors in Hex:")
        self.instruction_label.setStyleSheet("color: white;")

        self.input_label1 = QLabel("Primary Color:")
        self.input_text1 = QLineEdit()
        self.input_text1.setStyleSheet("background-color: white;")
        self.input_text1.setText("4C721D")
        self.input_label1.setStyleSheet("color: white;")

        self.input_label2 = QLabel("Offset Color:")
        self.input_text2 = QLineEdit()
        self.input_text2.setStyleSheet("background-color: white;")
        self.input_text2.setText("FFFFFF")
        self.input_label2.setStyleSheet("color: white;")

        self.confirm_button = QPushButton('Enter')
        self.confirm_button.setStyleSheet("background-color: white;")
        self.confirm_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(self.instruction_label)
        layout.addWidget(self.input_label1)
        layout.addWidget(self.input_text1)
        layout.addWidget(self.input_label2)
        layout.addWidget(self.input_text2)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)

    def get_inputs(self):
        return self.input_text1.text(), self.input_text2.text()

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
MainWindow.open_windows.append(window)  # Add the initial MainWindow to the list
app.exec()
