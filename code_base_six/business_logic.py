from IO_ops_v2 import Read, Write
from load_store_ops_v2 import Load, Store
from control_ops_v2 import Branch, BranchNeg, BranchZero, Halt 
from arithmetic_ops_v2 import Add, Subtract, Divide, Multiply

def Check_for_Operation(digits, mem, window):
    opp_nums = int(digits[0:2])
    act_nums = int(digits[2:4])
    if opp_nums == 10: # Read
        if Read(act_nums,mem,window):
            pass
        return False

    if opp_nums == 11: # Write
        if Write(act_nums,mem,window):
            pass
        return False

    if opp_nums == 20: # Load
        if Load(act_nums,mem,window):
            window.appendOutput(f'Loading {mem.get_acc()} into the accumulator')
        return False

    if opp_nums == 21: # Store
        if Store(act_nums,mem,window):
            window.appendOutput(f'Succefully stored value')
        return False

    if opp_nums == 30: # Add
        if Add(act_nums,mem,window):
            window.appendOutput(f'Updated Value: {mem.get_acc()}')
        return False

    if opp_nums == 31: # Subtract
        if Subtract(act_nums,mem,window):
            window.appendOutput(f'Updated Value: {mem.get_acc()}')
        return False

    if opp_nums == 32: # Divide
        if Divide(act_nums,mem,window):
            window.appendOutput(f'Updated Value: {mem.get_acc()}')
        return False

    if opp_nums == 33: # Multiply
        if Multiply(act_nums,mem,window):
            window.appendOutput(f'Updated Value: {mem.get_acc()}')
        return False

    if opp_nums == 40: # Branch
        if Branch(act_nums,mem,window):
            return True
        return False

    if opp_nums == 41: # BranchNeg
        if BranchNeg(act_nums,mem,window):
            return True
        return False

    if opp_nums == 42: # BranchZero
        if BranchZero(act_nums,mem,window):
            return True
        return False

    if opp_nums == 43: # Halt
        Halt(mem)

    else:
        return False


