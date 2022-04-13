import tupperware
import time
import student

class Counter:
    
    def __init__ (self):
        self.mCount = 0

def addAges(s, c):
    c.mCount += int(s.mAge)
    
def printFirstName(self, c):
    print(self.mFirst)
    
    
def inserting(sList):
    start_time = time.time()
    
    print("Program Status: Creating student list")
    fin = open("textfiles/InsertNamesSmall.txt")
            
    for line in fin:
        words = line.split()
        s = student.Student(words[0], words[1], words[2], words[3], words[4])
        stud = sList.Insert(s)
        
        if stud == False:
            other_stud = sList.Retrieve(s)
            print(other_stud.duplicate_msg(s))
            
    end_time = time.time()
    print("Total time for inserting students was: ", end_time - start_time)
    return sList
    fin.close()
    
'''def retrieving(sList, file):
    
    for line in file:
        ssn = line.strip()
        sList.Exists(ssn)

'''
def deleting(sList, file):
    
    
    
    t1 = time.time()
    fin = open("textfiles/DeleteNames.txt")
    for line in fin:
        ssn = line.strip()
        ok = sList.Delete(ssn)
        if ok == True:
            print("true")
    
        if ok == False:
            print("false")
    t2 = time.time()
    print("Total delete time was: ", t2 - t1)
    
def main():
    
    sList = tupperware.Tupperware()
    inserting(sList)
    time_start = time.time()
    c = Counter()
    sList.Traverse(addAges, c)
    print("Average age is:" , c.mCount / sList.Size())
    time_end = time.time()
    print("Time for average age calculation is: ", time_end - time_start)
    
    #T_file = open("textfiles/RetrieveNames.txt")
    #retrieving(sList, T_file)
    D_file = open("textfiles/DeleteNames.txt")
    deleting(sList, D_file)
    
if __name__ == "__main__":
    main()
