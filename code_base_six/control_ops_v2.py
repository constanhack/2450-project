from data_model import DataModel

def Branch(act_nums,mem,window):
    '''Branch to a specific location in memory'''
    if No_Infinite_Branching(mem.get_pc(), act_nums,mem):
        if Check_Branch_In_Range(act_nums, mem):
            mem.set_pc(act_nums)
            window.appendOutput(f'Branching to register {mem.get_pc()}')
            return True
        else: 
            window.appendOutput("Branch Range Error: Can't branch to location outside of memory")
            return False
    else:
        window.appendOutput("Infinite Branching Error: Can't branch to same line as branch call")
        return False

def BranchNeg(act_nums,mem,window):
    '''Branch to a specific location in memory if the accumulator is negative.'''
    if No_Infinite_Branching(mem.get_pc(), act_nums,mem):
        if mem.get_acc() < 0:
            if Check_Branch_In_Range(act_nums, mem):
                mem.set_pc(act_nums)
                window.appendOutput(f'Branching to register {mem.get_pc()}')
                return True
            else: 
                window.appendOutput("Branch Range Error: Can't branch to location outside of memory")
                return False
        else:
            window.appendOutput("Branch Unsuccessful: Accumulator is not 0")
            return False
    else:
        window.appendOutput("Infinite Branching Error: Can't branch to same line as branch call")
        return False

def BranchZero(act_nums,mem,window):
    '''Branch to a specific location in memory if the accumulator is zero.'''
    if No_Infinite_Branching(mem.get_pc(), act_nums,mem):
        if mem.get_acc() == 0:
            if Check_Branch_In_Range(act_nums, mem):
                mem.set_pc(act_nums)
                window.appendOutput(f'Branching to register {mem.get_pc()}')
                return True
            else: 
                window.appendOutput("Branch Range Error: Can't branch to location outside of memory")
                return False
        else:
            window.appendOutput("Branch Unsuccessful: Accumulator is not 0")
            return False
    else:
        window.appendOutput("Infinite Branching Error: Can't branch to same line as branch call")
        return False

def Halt(mem):
    '''Pause the program'''
    mem._private_PC = 'HALT'
    return
    
def No_Infinite_Branching(PC, act_nums,mem):
    '''Checks to make sure the branch is to a different location, otherwise it Halts'''
    if PC != act_nums:
        return True
    else:
        return Halt(mem)
    
def Check_Branch_In_Range(act_nums,mem):
    if act_nums < mem.mem_size:
        return True
    else:
        return Halt(mem)
