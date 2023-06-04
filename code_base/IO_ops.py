from memory_and_file_ops import Get_Value

def Read(act_nums,MEM):
    #Read a word from the keyboard into a specific location in memory.
    word = input("Please enter a word: ")
    while True:
        if len(word) != 5:
            print("Error, word length must be 5 charactes. Ex: '+1873'")
            word = input("Please enter a word: ")
        if word[0] not in ('+','-'):
            print("Error, word must begin with '-' or '+'")
        try:
            int(word[2:5])
            break
        except ValueError:
            print("Error, last 4 characters must be digits")
            word = input("Please enter a word: ")
        
         
    MEM[act_nums] = word
    return MEM

def Write(act_nums,MEM):
    #Write a word from a specific location in memory to screen.
    word = MEM[act_nums]
    print(word)
    return MEM