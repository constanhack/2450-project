from memory_and_file_ops import Get_Value

def Branch(act_nums,MEM,PC):
    pass

def Branchneg(act_nums,MEM,ACC,PC):
    if ACC[0] == '-':
        return[MEM,ACC,int(act_nums),True]
    return [MEM,ACC,PC,False]

def Branchzero(act_nums,MEM,ACC,PC):
    pass

def Halt():
    exit()