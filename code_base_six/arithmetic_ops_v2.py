from data_model import DataModel
from control_ops_v2 import Halt

def Add(act_nums,mem,window):
    """Adds a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)"""
    ACC = mem.get_acc()
    window.appendOutput(f'Adding {mem.get_mem_value(act_nums)} to {ACC}')
    ACC += mem.get_mem_value(act_nums)
    if Check_No_Overflow(ACC,mem):
        mem.set_acc(ACC)
        return True
    else:
        window.appendOutput("Overflow Error: Value added exceeded 999999")
        return False

def Subtract(act_nums,mem,window):
    """Subtracts a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)"""
    ACC = mem.get_acc()
    window.appendOutput(f'Subtracting {mem.get_mem_value(act_nums)} from {ACC}')
    ACC -= mem.get_mem_value(act_nums)
    if Check_No_Overflow(ACC,mem):
        mem.set_acc(ACC)
        return True
    else:
        window.appendOutput("Overflow Error: Value added exceeded 999999/-999999")
        return False

def Divide(act_nums,mem,window):
    """Divides the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator)."""
    ACC = mem.get_acc()
    if mem.get_mem_value(act_nums) == 0:
        print("Division By Zero Error: Cannot divide by 0\nHalting Program")
        Halt(mem)
    else:
        window.appendOutput(f'Dividing {ACC} by {mem.get_mem_value(act_nums)}')
        ACC //= mem.get_mem_value(act_nums)

        if Check_No_Overflow(ACC,mem):
            mem.set_acc(ACC)
            return True
    return False

def Multiply(act_nums,mem,window):
    """Multiplies a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)."""
    ACC = mem.get_acc()
    window.appendOutput(f'Multiplying {ACC} by {mem.get_mem_value(act_nums)}')
    ACC *= mem.get_mem_value(act_nums)
    if Check_No_Overflow(ACC,mem):
        mem.set_acc(ACC)
        return True
    else:
        window.appendOutput("Overflow Error: Value added exceeded 999999/-999999")
        return False

def Check_No_Overflow(ACC,mem):
    '''Checks for overflow values (Greater than 999999 or less than -999999)'''
    if ACC > 999999 or ACC < -999999:
        print("Overflow Error: Result exceeded available space\nHalting Program")
        Halt(mem)
    else:
        return True
