from memory_and_file_ops import Get_Value

def Load(act_nums,MEM,ACC):
    #Load a word from a specific location in memory into the accumulator.
    word = MEM[act_nums]
    ACC = word
    return MEM,ACC

def Store(act_nums,MEM,ACC):
    #Store a word from the accumulator into a specific location in memory.
    MEM[act_nums] = ACC
    return MEM, ACC