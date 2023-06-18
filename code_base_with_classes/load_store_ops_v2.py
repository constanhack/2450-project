from data_model import DataModel

def Load(act_nums,mem):
    #Load a word from a specific location in memory into the accumulator.
    word = mem.get_mem_value(act_nums)
    if mem.validate_value(word):
            mem.set_acc(word)
            return True
    exit()

def Store(act_nums,mem):
    #Store a word from the accumulator into a specific location in memory.
    word = mem.get_acc()
    if mem.validate_value(word):
        mem.set_mem_value(word,act_nums)
        return True
    exit()