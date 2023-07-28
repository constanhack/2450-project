from memory_and_file_ops import Get_Value
from control_ops import Halt

def Add(act_nums,MEM,ACC):
    """Adds a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)"""
    ACC = int(ACC)
    print(f'Adding {int(MEM[act_nums])} to {ACC}')
    ACC += int(MEM[act_nums])
    if Check_No_Overflow(ACC):
        sign = '-' if ACC < 0 else '+'
        result = sign + str(ACC)[1:].zfill(4) if ACC < 0 else sign + str(ACC).zfill(4)
        return [MEM, result]

def Subtract(act_nums,MEM,ACC):
    """Subtracts a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)"""
    ACC = int(ACC)
    print(f'Subtracting {int(MEM[act_nums])} from {ACC}')
    ACC -= int(MEM[act_nums])
    if Check_No_Overflow(ACC):
        sign = '-' if ACC < 0 else '+' 
        result = sign + str(ACC)[1:].zfill(4) if ACC < 0 else sign + str(ACC).zfill(4)
        return [MEM, result]

def Divide(act_nums,MEM,ACC):
    """Divides the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator)."""
    ACC = int(ACC)
    if int(MEM[act_nums]) == 0:
        print("Division By Zero Error: Cannot divide by 0\nHalting Program")
        Halt()
    else:
        print(f'Dividing {ACC} by {int(MEM[act_nums])}')
        ACC //= int(MEM[act_nums])
        # remainder = ACC - float(int(ACC))
        # if remainder > 0:
        #     print(f'Remainder of {remainder} is being removed')
        #     ACC = int(ACC)
        if Check_No_Overflow(ACC):
            sign = '-' if ACC < 0 else '+' 
            result = sign + str(ACC)[1:].zfill(4) if ACC < 0 else sign + str(ACC).zfill(4)
            return [MEM, result]

def Multiply(act_nums,MEM,ACC):
    """Multiplies a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)."""
    ACC = int(ACC)
    print(f'Multiplying {ACC} by {int(MEM[act_nums])}')
    ACC *= int(MEM[act_nums])
    if Check_No_Overflow(ACC):
        sign = '-' if ACC < 0 else '+' 
        result = sign + str(ACC)[1:].zfill(4) if ACC < 0 else sign + str(ACC).zfill(4)
        return [MEM, result]

def Check_No_Overflow(ACC):
    '''Checks for overflow values (Greater than 9999 or less than -9999)'''
    if ACC > 9999 or ACC < -9999:
        print("Overflow Error: Result exceeded available space\nHalting Program")
        Halt()
    else:
        return True