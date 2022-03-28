import random
def alist (length):
    a_list = list(range(0, length))
    print(a_list)
    
#BLIST WORKS
def blist (length):
    randomlist = []
    for i in range(length):
        n = random.randint(1,length)
        randomlist.append(n)
    print(randomlist)
    
def main():
    print(alist(8))
    print(blist(8))
    
main()