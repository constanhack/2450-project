def Branch(act_nums,MEM):
    '''Branch to a specific location in memory'''
    return[MEM, int(act_nums), True]

def BranchNeg(act_nums,MEM,ACC,PC):
    '''Branch to a specific location in memory if the accumulator is negative.'''
    if ACC[0] == '-':
        return[MEM,ACC,int(act_nums),True]
    return [MEM, ACC, PC, False]

def BranchZero(act_nums, MEM, ACC, PC):
    '''Branch to a specific location in memory if the accumulator is zero.'''
    if ACC[1:5] == '0000':
        return[MEM, ACC, int(act_nums), True]
    return [MEM, ACC, PC, False]

def Halt():
    '''Pause the program'''
    exit()