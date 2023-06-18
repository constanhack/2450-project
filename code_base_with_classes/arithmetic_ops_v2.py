from data_model import DataModel
from control_ops_v2 import Halt

def Add(act_nums,mem):
    """Adds a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)"""
    ACC = mem.get_acc()
    print(f'Adding {mem.get_mem_value(act_nums)} to {ACC}')
    ACC += mem.get_mem_value(act_nums)
    if Check_No_Overflow(ACC):
        mem.set_acc(ACC)
        return True
    return False

def Subtract(act_nums,mem):
    """Subtracts a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)"""
    ACC = mem.get_acc()
    print(f'Subtracting {mem.get_mem_value(act_nums)} from {ACC}')
    ACC -= mem.get_mem_value(act_nums)
    if Check_No_Overflow(ACC):
        mem.set_acc(ACC)
        return True
    return False

def Divide(act_nums,mem):
    """Divides the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator)."""
    ACC = mem.get_acc()
    if mem.get_mem_value(act_nums) == 0:
        print("Division By Zero Error: Cannot divide by 0\nHalting Program")
        Halt()
    else:
        print(f'Dividing {ACC} by {mem.get_mem_value(act_nums)}')
        ACC //= mem.get_mem_value(act_nums)

        if Check_No_Overflow(ACC):
            mem.set_acc(ACC)
            return True
        
    return False

def Multiply(act_nums,mem):
    """Multiplies a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)."""
    ACC = mem.get_acc()
    print(f'Multiplying {ACC} by {mem.get_mem_value(act_nums)}')
    ACC *= mem.get_mem_value(act_nums)
    if Check_No_Overflow(ACC):
        mem.set_acc(ACC)
        return True
        
    return False

def Check_No_Overflow(ACC):
    '''Checks for overflow values (Greater than 9999 or less than -9999)'''
    if ACC > 9999 or ACC < -9999:
        print("Overflow Error: Result exceeded available space\nHalting Program")
        Halt()
    else:
        return True