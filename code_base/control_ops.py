def Branch(act_nums,MEM, PC):
    '''Branch to a specific location in memory'''
    if No_Infinite_Branching(PC, act_nums):
        return[MEM, int(act_nums), True]

def BranchNeg(act_nums,MEM,ACC,PC):
    '''Branch to a specific location in memory if the accumulator is negative.'''
    if No_Infinite_Branching(PC, act_nums):
        if ACC[0] == '-' and ACC[1:5] != '0000':
            return[MEM,ACC,int(act_nums),True]
        return [MEM, ACC, PC, False]

def BranchZero(act_nums, MEM, ACC, PC):
    '''Branch to a specific location in memory if the accumulator is zero.'''
    if No_Infinite_Branching(PC, act_nums):
        if ACC[1:5] == '0000':
            return[MEM, ACC, int(act_nums), True]
        return [MEM, ACC, PC, False]
    

def Halt():
    '''Pause the program'''
    exit()
    
def No_Infinite_Branching(PC, act_nums):
    '''Checks to make sure the branch is to a different location, otherwise it Halts'''
    if PC != int(act_nums):
        return True
    else:
        print("Error: Infinite branching. Halting Program")
        Halt()