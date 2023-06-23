import sys
import time
from PyQt6 import QtWidgets, uic
from data_loader import DataLoader
from data_model import DataModel
from driver import main

from UVSim import Ui_MainWindow 

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        self.setFixedSize(self.size())
        self.ChooseFile.clicked.connect(self.chooseFileButtonClicked)
        self.Clear.clicked.connect(self.clearFilePath)
        self.Start.clicked.connect(self.submitFilePath)
        self.Enter.setCheckable(True)
        self.Enter.setChecked(False)
        self.Enter.clicked.connect(self.enterClicked)
        self.Enter.setEnabled(False)

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


    def displayOutput(self,value):
        self.OutputText.clear()
        self.OutputText.setText(value)

    def appendOutput(self,value):
        self.OutputText.append(value)

    def getInput(self):
        self.Enter.setEnabled(True)
        while self.Enter.isChecked == False:
            pass
            



app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()


