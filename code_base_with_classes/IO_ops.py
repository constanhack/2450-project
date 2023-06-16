from data_model import DataModel

def Read(act_nums,mem):
    #Read a word from the keyboard into a specific location in memory.
    explanation = 'Type "q" to exit'
    while True:
        word = input("Please enter a word: ")
        if word in ['Q','q']:
            print("Exiting program")
            exit()
        try:
            int(word)
        except ValueError:
            print("Error, last 4 characters must be digits")
            print(explanation)
            continue
        if int(word) < -9999 or int(word) > 9999: 
            print("Error, input outside of valid range of -9999 to 9999")
            print(explanation)
            continue
        break
        
    mem.set_mem_value(int(word),act_nums)
    return True

def Write(act_nums,mem):
    #Write a word from a specific location in memory to screen.
    word = mem.get_mem_value(act_nums)
    try:
        int(word)
    except ValueError:
        print("Error, last 4 characters must be digits")
        exit()
    if int(word) < -9999 or int(word) > 9999: 
        print("Error, data outside of valid range of -9999 to 9999")
        exit()
    
    print(word)
    return True