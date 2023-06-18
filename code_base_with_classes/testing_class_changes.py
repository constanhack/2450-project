from data_loader import DataLoader
from data_model import DataModel
from IO_ops_v2 import Read, Write
from load_store_ops_v2 import Load, Store
from control_ops_v2 import Branch, BranchNeg, BranchZero, Halt 
from arithmetic_ops_v2 import Add, Subtract, Divide, Multiply


print('Please select the txt file you want to test')
data = DataLoader()
mem = DataModel(data.get_data())


def Check_for_Operation(digits):
    opp_nums = int(digits[0:2])
    act_nums = int(digits[2:4])
    if opp_nums == 10: # Read
        print(f'Running Read')
        if Read(act_nums,mem):
            pass
        return False

    if opp_nums == 11: # Write
        print(f'Running Write')
        if Write(act_nums,mem):
            pass
        return False

    if opp_nums == 20: # Load
        print(f'Running Load')
        if Load(act_nums,mem):
            print(f'Loading {mem.get_acc()} into the accumulator')
        return False

    if opp_nums == 21: # Store
        print(f'Running Store')
        if Store(act_nums,mem):
            print(f'Succefully stored value')
        return False

    if opp_nums == 30: # Add
        print(f'Running Add')
        if Add(act_nums,mem):
            print(f'Updated Value: {mem.get_acc()}')
        return False

    if opp_nums == 31: # Subtract
        print(f'Running Subtract')
        if Subtract(act_nums,mem):
            print(f'Updated Value: {mem.get_acc()}')
        return False

    if opp_nums == 32: # Divide
        print(f'Running Divide')
        if Divide(act_nums,mem):
            print(f'Updated Value: {mem.get_acc()}')
        return False

    if opp_nums == 33: # Multiply
        print(f'Running Multiply')
        if Multiply(act_nums,mem):
            print(f'Updated Value: {mem.get_acc()}')
        return False

    if opp_nums == 40: # Branch
        print(f'Running Branch')
        if Branch(act_nums,mem):
            return True
        return False

    if opp_nums == 41: # BranchNeg
        print(f'Running BranchNeg')
        if BranchNeg(act_nums, mem):
            return True
        return False

    if opp_nums == 42: # BranchZero
        print(f'Running BranchZero')
        if BranchZero(act_nums, mem):
            return True
        return False

    if opp_nums == 43: # Halt
        print(f'Running Halt')
        Halt()

    else:
        return False
    


while mem.get_pc() < mem.mem_size:
    pc_location = mem.get_pc()
    print(f"pc number {pc_location} ACC value {mem.get_acc()} type of acc = {type(mem._private_ACC)}")
    if mem.get_mem_value(pc_location) == 0:
        mem.increment_pc()
        continue

    
    # if len(Get_Value(PC,MEM)) != 5:
    #     print(f'Value {Get_Value(PC,MEM)} at address 0{PC} is an invalid length.  Shutting Down')
    #     exit()

    # if Get_Value(PC,MEM)[:1] != '+' and Get_Value(PC,MEM)[:1] != '-':
    #     print(f'Value {Get_Value(PC,MEM)} at address 0{PC} does not have a valid sign (+,-). Shutting Down')
    #     exit()

    if mem.get_mem_value(pc_location) >= 0:
        branched = Check_for_Operation(str(mem.get_mem_value(pc_location)))
        
        if branched:
            print(f'Branching to register {mem.get_pc()}')
            continue
            

    mem.increment_pc()