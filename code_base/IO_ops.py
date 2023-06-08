from memory_and_file_ops import Get_Value

def Read(act_nums,MEM):
    #Read a word from the keyboard into a specific location in memory.
    explanation = 'Type "q" to exit'
    while True:
        word = input("Please enter a word: ")
        if word in ['Q','q']:
            print("Exiting program")
            exit()
        if len(word) != 5:
            print("Error, word length must be 5 charactes. Ex: '+1873'")
            print(explanation)
            continue
        if word[0] not in ('+','-'):
            print("Error, word must begin with '-' or '+'")
            print(explanation)
            continue
        try:
            int(word[1:5])
            break
        except ValueError:
            print("Error, last 4 characters must be digits")
            print(explanation)
            continue
        
         
    MEM[act_nums] = word
    return MEM

def Write(act_nums,MEM):
    #Write a word from a specific location in memory to screen.
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
    
    print(word)
    return MEM