import time

Q_bank = {}
A_bank = {}

file = open("questions.txt", "r")
for line in file:
    k, v = line.strip().split("=")
    Q_bank [k.strip()] = v.strip()
file.close()

file = open("answers.txt", "r")
for line in file:
    k, v = line.strip().split("=")
    A_bank [k.strip()] = v.strip()
file.close()

print("Question bank is: \n" , Q_bank) #DELETE LATER
print("Answer bank is: \n" , A_bank)
timer1 = time.time()
answered = False
for questions in Q_bank:
    answered = False
    while answered == False:
        print(Q_bank[questions])
        question = input("Answer here: ")
        if question == "a": #Answer goes here
            answered = True
        else:
            print("Wrong, try again: ")
            question
timer2 = time.time()
print("Total time for answering questions was: " , timer2 - timer1)
