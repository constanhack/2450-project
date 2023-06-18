from data_model import DataModel

def Read(act_nums,mem):
    #Read a word from the keyboard into a specific location in memory.
    while True:
        word = input("Please enter a word: (Type 'q' to exit) ")
        if word in ['Q','q']:
            print("Exiting program")
            exit()
        if mem.validate_value(word):
            break

        
    mem.set_mem_value(int(word),act_nums)
    return True

def Write(act_nums,mem):
    #Write a word from a specific location in memory to screen.
    word = mem.get_mem_value(act_nums)
    if mem.validate_value(word):
        print(word)
        return True
    exit()