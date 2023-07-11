import sys
import time
from PyQt6 import QtWidgets, uic
from data_loader import DataLoader
from data_model import DataModel
from driver import main
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLineEdit, QApplication, QDialog, QVBoxLayout, QPushButton, QLabel, QTableWidget, QTableWidgetItem
from UVSim import Ui_MainWindow 
from PyQt5.QtGui import QColor


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.ChooseFile.clicked.connect(self.chooseFileButtonClicked)
        self.Clear.clicked.connect(self.clearFilePath)
        self.Start.clicked.connect(self.submitFilePath)
        self.ColorSelect.clicked.connect(self.colorBox)

        #self.InputText = QLineEdit(self)

    def chooseFileButtonClicked(self):
        self.OutputText.clear()
        self._data = DataLoader()
        ##self._mem = DataModel(data.get_data())
        self.FilePath.setText(self._data.get_file_path())

    def clearFilePath(self):
        self.OutputText.clear()
        self.FilePath.clear()

    def submitFilePath(self):
        self.OutputText.clear()
        filepath = self.FilePath.text()
        print(filepath)
        if filepath:
            editWindow = FileEditBox(window)
            editWindow.setModal(True)
            if editWindow.exec() == QDialog.DialogCode.Accepted:
                main(DataModel(self._data.get_data()), window)
                self.appendOutput('Program Complete\nSelect a file to run again')
        else:
            self.OutputText.setText('Please Select A File To start')

    
    def enterClicked(self):
        self.Enter.setChecked(True)
        

        # reg_ex = QRegExp("^-?[0-9]{4}$")
        # input_validator = QRegExpValidator(reg_ex, self.InputText)
        # self.InputText.setValidator(input_validator)

        user_input = self.getInput()
        


        # while user_input == "":
        #     user_input = self.getInput()
            
        # print(input)
        #self.InputText.setValidator()
        #self.appendOutput("Inputted " + input)

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
            if is_valid_hex(user_input1) and is_valid_hex(user_input2):
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

def is_valid_hex(color):
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
                        self.setItem(row_anchor + indx_row, column_anchor + indx_col, item)
            super().keyPressEvent(event)

class FileEditBox(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.window_width, self.window_height = 200, 500
        self.setMinimumSize(self.window_width, self.window_height)
        self.setStyleSheet('''
            QWidget {
                font-size: 12px;
            }
        ''')
        print(parent._data.get_data().values())        

        self.layout = {}
        self.layout['main'] = QVBoxLayout()
        self.setLayout(self.layout['main'])

        self.table = TableWidget(100, 1)
        self.table.setHorizontalHeaderLabels(['Values'])
        self.table.setSortingEnabled(False)
        rowLabels = []
        i = 0
        for item in parent._data.get_data().values():
             rowLabels.append(str(i))
             self.table.setItem(i,0,QTableWidgetItem(str(item)))
             i += 1
        self.table.setVerticalHeaderLabels(rowLabels)
        self.layout['main'].addWidget(self.table)

        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.accept)
        self.layout['main'].addWidget(self.submit_button)

class ColorInputBox(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Change Color")

        self.instruction_label = QLabel("Please enter colors in Hex:")
        self.instruction_label.setStyleSheet("color: white;")


        self.input_label1 = QLabel("Color 1:")
        self.input_text1 = QLineEdit()
        self.input_text1.setStyleSheet("background-color: white;")
        self.input_text1.setText("4C721D")
        self.input_label1.setStyleSheet("color: white;")

        self.input_label2 = QLabel("Color 2:")
        self.input_text2 = QLineEdit()
        self.input_text2.setStyleSheet("background-color: white;")
        self.input_text2.setText("FFFFFF")
        self.input_label2.setStyleSheet("color: white;")

        self.confirm_button = QPushButton('Enter')
        self.confirm_button.setStyleSheet("color: white;")
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
app.exec()


