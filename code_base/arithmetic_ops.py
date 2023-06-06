from memory_and_file_ops import Get_Value

def Add(act_nums,MEM,ACC):
    """Adds a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)"""
    ACC = int(ACC)
    ACC += int(MEM[act_nums])
    return [MEM, ACC]

def Subtract(act_nums,MEM,ACC):
    """Subtracts a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)"""
    ACC = int(ACC)
    ACC -= int(MEM[act_nums])
    return [MEM, ACC]

def Divide(act_nums,MEM,ACC):
    """Divides the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator)."""
    ACC = int(ACC)
    ACC /= int(MEM[act_nums])
    return [MEM, ACC]

def Multiply(act_nums,MEM,ACC):
    """Multiplies a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)."""
    ACC = int(ACC)
    ACC *= int(MEM[act_nums])
    return [MEM, ACC]