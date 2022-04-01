#extra credit assignment #1
import time
import random


exponent_dictionary = {"What is 2** 0 ? ": "1","What is 2** 1 ? ": "2", "What is 2** 2 ? ": "4","What is 2** 3 ? ": "8", "What is 2** 4 ? ": "16",
                       "What is 2** 5 ? ": "32", "What is 2** 6 ? ": "64", "What is 2** 7 ? ": "128", "What is 2** 8 ? ": "256", "What is 2** 9 ? ": "512",
                       "What is 2** 10 ? ": "1k","What is 2** 11 ? ": "2k","What is 2** 12 ? ": "4k","What is 2** 13 ? ": "8k", "What is 2** 14 ? ": "16k",
                       "What is 2** 15 ? ": "32k","What is 2** 16 ? ": "64k","What is 2** 17 ? ": "128k","What is 2** 18 ? ": "256k",
                       "What is 2** 19 ? ": "512k","What is 2** 20 ? ": "1m","What is 2** 21 ? ": "2m", "What is 2** 22 ? ": "4m",
                       "What is 2** 23 ? ": "8m","What is 2** 24 ? ": "16m","What is 2** 25 ? ": "32m", "What is 2** 26 ? ": "64m", "What is 2** 27 ? ": "128m",
                       "What is 2** 28 ? ": "256m","What is 2** 29 ? ": "512m","What is 2** 30 ? ": "1b","What is 2** 31 ? ": "2b", "What is 2** 32 ? ": "4b",
                       "What is 2** 33 ? ": "8b","What is 2** 34 ? ": "16b","What is 2** 35 ? ": "32b", "What is 2** 36 ? ": "64b", "What is 2** 37 ? ": "128b",
                       "What is 2** 38 ? ": "256b","What is 2** 39 ? ": "512b","What is 2** 40 ? ": "1t","What is 2** 41 ? ": "2t", "What is 2** 42 ? ": "4t",
                       "What is 2** 43 ? ": "8t","What is 2** 44 ? ": "16t","What is 2** 45 ? ": "32t", "What is 2** 46 ? ": "64t", "What is 2** 47 ? ": "128t",
                       "What is 2** 48 ? ": "256t", "What is 2** 49 ? ": "512t"}


print("Exponent Quiz Time! Put the approx. answers & lowercase letters!")

def getKeys(xdict):
    key_list =[]
    for key in xdict.keys():
        key_list.append(key)
    
    return key_list

def main():
    
    list_count = 0
    
    t1 = time.time()
    
    key_list = getKeys(exponent_dictionary)
    random.shuffle(key_list)
    for key in key_list:
        user_input = input(key)
        list_count += 1
        while user_input != exponent_dictionary[key]:
                user_input = input("Wrong! Try again:")
                

    
    t2 = time.time()
    
    print("Total time:", t2 - t1)
    print(list_count)
if __name__ == "__main__":
    main()           
        
    


