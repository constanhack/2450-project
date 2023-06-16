from data_model import DataModel

def Load(act_nums,mem):
    #Load a word from a specific location in memory into the accumulator.
    word = mem.get_mem_value(act_nums)
    try:
        int(word)
    except ValueError:
        print("Error, last 4 characters must be digits")
        exit()
    if int(word) < -9999 or int(word) > 9999: 
        print("Error, data outside of valid range of -9999 to 9999")
        exit()

    mem.set_acc(int(word))
    return True

def Store(act_nums,mem):
    #Store a word from the accumulator into a specific location in memory.
    word = mem.get_acc()
    try:
        int(word)
    except ValueError:
        print("Error, last 4 characters must be digits")
        exit()
    if int(word) < -9999 or int(word) > 9999: 
        print("Error, data outside of valid range of -9999 to 9999")
        exit()
    mem.set_mem_value(int(word),act_nums)
    print(f"{mem.get}")
    return True