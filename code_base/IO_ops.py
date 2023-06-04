from memory_and_file_ops import Get_Value

def Read(act_nums,MEM):
    #Read a word from the keyboard into a specific location in memory.
    word = input("Please enter a word: ")
    MEM[act_nums] = word
    return MEM

def Write(act_nums,MEM):
    #Write a word from a specific location in memory to screen.
    word = MEM[act_nums]
    print(word)
    return MEM