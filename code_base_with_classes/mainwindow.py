import sys
import time
from PyQt6 import QtWidgets, uic
from data_loader import DataLoader
from data_model import DataModel
from driver import main
from PyQt6.QtWidgets import QWidget, QLineEdit, QApplication, QDialog, QVBoxLayout, QPushButton, QLabel
from UVSim import Ui_MainWindow 


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
        data = DataLoader()
        self._mem = DataModel(data.get_data())
        self.FilePath.setText(data.get_file_path())

    def clearFilePath(self):
        self.OutputText.clear()
        self.FilePath.clear()

    def submitFilePath(self):
        self.OutputText.clear()
        filepath = self.FilePath.text()
        print(filepath)
        if filepath:
            main(self._mem, window)
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
        dialog = ColorInputBox(window)
        dialog.setModal(True)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            user_input1, user_input2 = dialog.get_inputs()

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


