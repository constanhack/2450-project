from config import MEM, ACC, PC
from memory_and_file_ops import File_Picker, Allocate_Memory, Get_Value
from IO_ops import Read, Write
from load_store_ops import Load, Store
from arithmetic_ops import Add, Subtract, Divide, Multiply
from control_ops import Branch, Branchneg, Branchzero, Halt




##placeholder for opperations
## replace return name, by actually calling the function and continue with the driver
def Check_for_Operation(digits):
    opp_nums = int(digits[0:2])
    if opp_nums == 10:


        return 'READ'
    if opp_nums == 11:


        return 'WRITE'
    if opp_nums == 20:


        return 'LOAD'
    if opp_nums == 21:


        return 'STORE'
    if opp_nums == 30:


        return 'ADD'
    if opp_nums == 31:


        return 'SUBTRACT'
    if opp_nums == 32:


        return 'DIVIDE'
    if opp_nums == 33:


        return 'MULTIPLY'
    if opp_nums == 40:


        return 'BRANCH'
    if opp_nums == 41:


        return 'BRANCHNEG'
    if opp_nums == 42:


        return 'BRANCHZERO'
    if opp_nums == 43:


        ## call halt
        exit()
    else:
        return False
    
file = open(File_Picker(),'r')

MEM = Allocate_Memory(file)


while True:
    if len(Get_Value(PC)) != 5:
        print(f'Value {Get_Value(PC)} at address 0{PC} is an invalid length.  Shutting Down')
        exit()
    if Get_Value(PC)[:1] != '+' and Get_Value(PC)[:1] != '-':
        print(f'Value {Get_Value(PC)} at address 0{PC} does not have a valid sign (+,-). Shutting Down')
        exit()

    sign = Get_Value(PC)[:1]
    if sign == '+':
        operation = Check_for_Operation(Get_Value(PC)[1:5])
        if operation:
            print(operation)

    PC += 1