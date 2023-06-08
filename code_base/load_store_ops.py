from memory_and_file_ops import Get_Value

def Load(act_nums,MEM,ACC):
    #Load a word from a specific location in memory into the accumulator.
    word = MEM[act_nums]
    if isinstance(word,str) == False:
        print("Error, invalid memory data. Exiting program")
        exit()
    if len(word) !=5:
        print("Error, invalid data. Exiting program.")
        exit()
    if word[0] not in ('+','-'):
        print('Error, word must begin with "+" or "-". Exiting program')
        exit()
    try:
        int(word[1:5])
    except ValueError:
        print("Error, last 4 digits are not numbers. Exiting program")
        exit()
    ACC = word
    return MEM,ACC

def Store(act_nums,MEM,ACC):
    #Store a word from the accumulator into a specific location in memory.
    word = ACC
    if isinstance(word,str) == False:
        print("Error, invalid memory data. Exiting program")
        exit()
    if len(word) !=5:
        print("Error, invalid data. Exiting program.")
        exit()
    if word[0] not in ('+','-'):
        print('Error, word must begin with "+" or "-". Exiting program')
        exit()
    try:
        int(word[1:5])
    except ValueError:
        print("Error, last 4 digits are not numbers. Exiting program")
        exit()
    MEM[act_nums] = ACC
    return MEM, ACC