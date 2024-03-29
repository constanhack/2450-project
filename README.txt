UVSim

A virual machine that can only interpret a machine language called BasicML.



About UVSim

The UVSim contains CPU, register, and main memory. 
An accumulator – a register into which information is put before the UVSim uses it in calculations
or examines it in various ways.
All the information in the UVSim is handled in terms of words.
A word is a signed four-digit decimal number, such as +123456, -567890. 
The UVSim is equipped with a 250-word memory, and these words are referenced by their location
numbers 000, 001, ..., 249. 
The BasicML program will be loaded into the main memory starting at location 000 before executing. 
Each instruction written in BasicML occupies one word of the UVSim memory (instruction are signed
six-digit decimal number). 
It is assumed that the sign of a BasicML instruction is always plus, but the sign of a data word
may be either plus or minus. 
Each location in the UVSim memory may contain an instruction, a data value used by a program or
an unused area of memory. 
The first three digits of each BasicML instruction are the operation code specifying the operation
to be performed.



BasicML Language

The first three digits of each BasicML instruction are the operation code specifying the operation
to be performed.

BasicML vocabulary defined as follows:

Input/Output Operations:
READ = 010 Read a word from the keyboard into a specific location in memory.
WRITE = 011 Write a word from a specific location in memory to screen.

Load/store Operations:
LOAD = 020 Load a word from a specific location in memory into the accumulator.
STORE = 021 Store a word from the accumulator into a specific location in memory.

Arithmetic Operations:
ADD = 030 Add a word from a specific location in memory to the word in the accumulator (leave the
result in the accumulator)
SUBTRACT = 031 Subtract a word from a specific location in memory from the word in the accumulator
(leave the result in the accumulator)
DIVIDE = 032 Divide the word in the accumulator by a word from a specific location in memory
(leave the result in the accumulator).
MULTIPLY = 033 multiply a word from a specific location in memory to the word in the accumulator
(leave the result in the accumulator).

Control Operations:
BRANCH = 040 Branch to a specific location in memory
BRANCHNEG = 041 Branch to a specific location in memory if the accumulator is negative.
BRANCHZERO = 042 Branch to a specific location in memory if the accumulator is zero.
HALT = 043 Pause the program

The last three digits of a BasicML instruction are the operand – the address of the memory location
containing the word to which the operation applies.



Prerequisites:

pytest
PyQt6
PySide6


How to Install pytest:

pytest requires: Python 3.7+ or PyPy3.

Run the following command in your command line:

pip install -U pytest

Check that you installed the correct version:

$ pytest --version
pytest 7.1.3


pytest Documentation:
https://docs.pytest.org/en/7.1.x/getting-started.html



How to install PyQt6:

PyQt6 requires: Python v3.6.1 or later.

Run the following commands in your command line

pip install pyqt6
Pip install pyqt6-tools

PyQt6 Documentation:
https://www.riverbankcomputing.com/static/Docs/PyQt6/


How to install PySide6:

Run the following commands in your command line

pyside6 requires: The Clang library (C-bindings), version 13.0 or higher

pip install pyside6

PySide6 Documentation:
https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/index.html


How to Run UVSim

Enter the following command into your terminal:

python mainwindow.py

Or, you can find and run the the file "mainwindow.py" in the "code_base_with_classes" folder.


How to Use UVSim

1.) Opening/Selecting BasicML Code File:
To open your BasicML code file, select the choose file button.
This will prompt you to choose a file from your folders.
This file should be a text file filled (by the user) with BasicML commands in it.
Then, select the start button. This should open a window pop-up which will allow you to check/edit your file.

2.) Editing BasicML File:
Follow step 1 to open a file. 
Now you can edit your BasicML code.
To edit the code, you can double click any box to manually change the value. 
Copy/Paste values:
You can copy/paste the value in a single box.
You can also paste multiple values. If you select a single box with a single click (and you already
have multiple values/lines on your computer's clipboard), do the paste command to paste multiple
values into mutiple boxes.
Copy: CTRL + C
Paste: CTRL + V
If your file is done being edited, press the "Submit" button to run the file.
You may also save your edited file by pressing the Save button, remember to do this before pressing "Submit"

3.) Running BasicML File:
Follow steps 1 and 2 to open/edit the file first.
If you had any read commands, another window will pop up and you will have to enter a BasicML code
as an input. Hit enter once you have finished typing the code. This same pop up will appear for
every read command you have. If you had no read commands
in your code, no new pop-ups will appear.
After this, the code will run and display the output to the output box.

4.) Clearing the Output Box:
If the output box is getting too cluttered, press the clear button.

5.) Change Window Colors:
To change the colors of the UVSim window, select the change colors button.
A window will pop up that already has the hexidecimal values of the colors that UVSim is currently using. 
The first color is the primary color and the second color is the offset color of the window.
Click in the two boxes to enter new hexidecimal values of your chosen colors.
Once you are happy with your choices, hit enter.

6.) Converting 4 Digit BasicML to 6-Digit BasicML
If you want to run a 4-digit BasicML file, the file must be converted to 6-digit BasicML in order for
it to run correctly. UVSim makes this easy, simply select your file using the choose file button, then
select the "Convert file to 6-digit" check box. When you press start, you will be able to view, edit,
run, and save the converted BasicML file.



How to Test UVSim

1. Make sure that pytest is installed.
2. Enter the following command into your terminal:

pytest



Test Files

There are two test files that you can use in the test_files folder to use in the UVSim: 
Test1.txt and Test2.txt.


Contributors

Jay
Skyler
Travis
Hailey
