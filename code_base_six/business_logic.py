from IO_ops_v2 import Read, Write
from load_store_ops_v2 import Load, Store
from control_ops_v2 import Branch, BranchNeg, BranchZero, Halt 
from arithmetic_ops_v2 import Add, Subtract, Divide, Multiply

def Check_for_Operation(digits, mem, window):
    try:
        opp_nums = int(digits[0:3])
        act_nums = int(digits[3:6])
    except ValueError: # Catch the value error created by improperly formatted BasicML code, skip line
        window.appendOutput('Value Error: A line in your BasicML code is not in 6 digit BasicML format\nSkipping line.')
        return False

    if opp_nums == 10: # Read
        # print('read')
        if Read(act_nums,mem,window):
            pass
        return False

    if opp_nums == 11: # Write
        # print('write')
        if Write(act_nums,mem,window):
            pass
        return False

    if opp_nums == 20: # Load
        # print('load')
        if Load(act_nums,mem,window):
            window.appendOutput(f'Loading {mem.get_acc()} into the accumulator')
        return False

    if opp_nums == 21: # Store
        # print('store')
        if Store(act_nums,mem,window):
            window.appendOutput(f'Succefully stored value')
        return False

    if opp_nums == 30: # Add
        # print('add')
        if Add(act_nums,mem,window):
            window.appendOutput(f'Updated Value: {mem.get_acc()}')
        return False

    if opp_nums == 31: # Subtract
        # print('sub')
        if Subtract(act_nums,mem,window):
            window.appendOutput(f'Updated Value: {mem.get_acc()}')
        return False

    if opp_nums == 32: # Divide
        # print('divide')
        if Divide(act_nums,mem,window):
            window.appendOutput(f'Updated Value: {mem.get_acc()}')
        return False

    if opp_nums == 33: # Multiply
        # print('multiply')
        if Multiply(act_nums,mem,window):
            window.appendOutput(f'Updated Value: {mem.get_acc()}')
        return False

    if opp_nums == 40: # Branch
        # print('branch')
        if Branch(act_nums,mem,window):
            return True
        return False

    if opp_nums == 41: # BranchNeg
        # print('branchneg')
        if BranchNeg(act_nums,mem,window):
            return True
        return False

    if opp_nums == 42: # BranchZero
        # print('branchzero')
        if BranchZero(act_nums,mem,window):
            return True
        return False

    if opp_nums == 43: # Halt
        Halt(mem)

    else:
        return False
