from data_model import DataModel

def Branch(act_nums,mem):
    '''Branch to a specific location in memory'''
    if No_Infinite_Branching(mem.get_pc(), act_nums):
        mem.set_pc(act_nums)
        return True
    return False

def BranchNeg(act_nums,mem):
    '''Branch to a specific location in memory if the accumulator is negative.'''
    if No_Infinite_Branching(mem.get_pc(), act_nums):
        if mem.get_acc() < 0:
            mem.set_pc(act_nums)
            return True
        return False

def BranchZero(act_nums, mem):
    '''Branch to a specific location in memory if the accumulator is zero.'''
    if No_Infinite_Branching(mem.get_pc(), act_nums):
        if mem.get_acc() == 0:
            mem.set_pc(act_nums)
            return True
        return False

def Halt():
    '''Pause the program'''
    exit()
    
def No_Infinite_Branching(PC, act_nums):
    '''Checks to make sure the branch is to a different location, otherwise it Halts'''
    if PC != act_nums:
        return True
    else:
        print("Error: Infinite branching. Halting Program")
        Halt()
