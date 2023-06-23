from memory_and_file_ops import File_Picker, Allocate_Memory, Get_Value
from IO_ops import Read, Write
from load_store_ops import Load, Store
from arithmetic_ops import Add, Subtract, Divide, Multiply
from control_ops import Branch, BranchNeg, BranchZero, Halt

print('Please select the txt file you want to test')
file = open(File_Picker(),'r')

MEM = Allocate_Memory(file)
ACC = '+0000'
PC = 0

def Check_for_Operation(digits):
    global MEM; global ACC; global PC; 
    opp_nums = int(digits[0:2])
    act_nums = digits[2:4]
    if opp_nums == 10: # Read
        print(f'Running Read')
        MEM = Read(act_nums,MEM)
        return False

    if opp_nums == 11: # Write
        print(f'Running Write')
        MEM = Write(act_nums,MEM)
        return False

    if opp_nums == 20: # Load
        print(f'Running Load')
        MEM, ACC = Load(act_nums,MEM,ACC)
        print(f'Loading {ACC} into the accumulator')
        return False

    if opp_nums == 21: # Store
        print(f'Running Store')
        MEM, ACC = Store(act_nums,MEM,ACC)
        return False

    if opp_nums == 30: # Add
        print(f'Running Add')
        MEM, ACC = Add(act_nums,MEM,ACC)
        print(f'Updated Value: {ACC}')
        return False

    if opp_nums == 31: # Subtract
        print(f'Running Subtract')
        MEM, ACC = Subtract(act_nums,MEM,ACC)
        print(f'Updated Value: {ACC}')
        return False

    if opp_nums == 32: # Divide
        print(f'Running Divide')
        MEM, ACC = Divide(act_nums,MEM,ACC)
        print(f'Updated Value: {ACC}')
        return False

    if opp_nums == 33: # Multiply
        print(f'Running Multiply')
        MEM, ACC = Multiply(act_nums,MEM,ACC)
        print(f'Updated Value: {ACC}')
        return False

    if opp_nums == 40: # Branch
        print(f'Running Branch')
        MEM, PC, branched = Branch(act_nums,MEM, PC)
        return branched

    if opp_nums == 41: # BranchNeg
        print(f'Running BranchNeg')
        MEM, ACC, PC, branched = BranchNeg(act_nums, MEM, ACC, PC)
        return branched

    if opp_nums == 42: # BranchZero
        print(f'Running BranchZero')
        MEM, ACC, PC, branched = BranchZero(act_nums, MEM, ACC, PC)
        return branched

    if opp_nums == 43: # Halt
        print(f'Running Halt')
        Halt()

    else:
        return False
    


while PC <100:
    if Get_Value(PC,MEM) == '+0000':
        PC+=1
        continue

    if len(Get_Value(PC,MEM)) != 5:
        print(f'Value {Get_Value(PC,MEM)} at address 0{PC} is an invalid length.  Shutting Down')
        exit()

    if Get_Value(PC,MEM)[:1] != '+' and Get_Value(PC,MEM)[:1] != '-':
        print(f'Value {Get_Value(PC,MEM)} at address 0{PC} does not have a valid sign (+,-). Shutting Down')
        exit()

    sign = Get_Value(PC,MEM)[:1]
    if sign == '+':
        branched = Check_for_Operation(Get_Value(PC,MEM)[1:5])
        #print(f'Branched status: {branched} PC num: {PC}')
        
        if branched:
            print(f'Branching to register {PC}')
            continue
            

    PC += 1