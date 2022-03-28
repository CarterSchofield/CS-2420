import random
import sys
import math

class Counter:
    def __init__(self):
        self.count = 0
    
def createRandomList(length):
    A = random.sample(range(0, length), length)
    return A

def createMostlySorted(length):
    A = createRandomList(length)
    A.sort()
    A[0], A[len(A)-1] = A[len(A)-1], A[0]
    return(A)

def bubbleSort(A, C):
    changed = True
    while changed == True:
        changed = False
        for i in range(len(A) - 1):
            C.count += 1
            if A[i] > A[i+1]:
                A[i],A[i+1] = A[i+1], A[i]
                changed = True
                
def shakerSort(A, C):
    changed = True
    while changed == True:
        changed = False
        for i in range(len(A)-1):
            C.count += 1
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                changed = True
        #one pass to left
        C.count+=1
        for i in range(len(A)-2, -1, -1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                changed = True

def countingSort(A, C):
    C.count = len(A)
    F = [0] * len(A)
    for V in A:
        F[V] += 1
    K = 0
    for i in range(len(F)):
        value = i
        count = F[i]
        for j in range(count):
            A[K] = value
            K += 1
            
def mergeSort(A, C):
    if len(A) <= 1:
        return
    #Break A into 2 halves
    mid = len(A)//2
    L = A[0:mid]
    R = A[mid:]
    #Sort the two halves
    mergeSort(L, C)
    mergeSort(R, C)
    #merge L and R back over A
    i = 0
    J = 0
    k = 0
    while i < len(L) and J < len(R):
        C.count +=1
        if L[i] <= R[J]:
            A[k] = L[i]
            i += 1
            k += 1
        else:
            A[k] = R[J]
            J += 1
            k += 1
    if len(L) > i:
        A[k:] = L[i:]
    else:
        A[k:] = R[J:]
        
def quickSortR(A, low, high, mod, C):
    if high - low <= 0:
        return
    if mod == True:
        mid = (low + high)//2
        A[low], A[mid] = A[mid], A[low]
    #1 pass
    pivot = low
    lmgT = low+1
    for i in range(low+1, high+1):
        C.count += 1
        if A[i] < A[pivot]:
            A[i], A[lmgT] = A[lmgT], A[i]
            lmgT += 1
    pivot = lmgT - 1
    A[low], A[pivot] = A[pivot], A[low]
    #Recurse
    quickSortR(A, low, pivot-1, mod, C)
    quickSortR(A, pivot+1, high, mod,  C)

def quickSort(A, C):
    quickSortR(A, 0, len(A)-1, False, C)
    
def modQuickSort(A, C):
    quickSortR(A, 0, len(A)-1, True, C)

def Format(X):
    if X!=0:
        X = math.log(X)/math.log(2)
    return X

def main():
    sys.setrecursionlimit(5000)
    sorts = [bubbleSort, shakerSort, countingSort, mergeSort, quickSort, modQuickSort]
    print("","", "", "","Bubble", "Shaker", "Counting", "MergeSort", "QuickSort", "ModifiedQuick")
    for s in range(3, 13):
        size = 2 ** s
        print("%02d" % (s), " ", end="")
        for sort in sorts:
            #A = createRandomList(size)
            A = createMostlySorted(size)
            C = Counter()
            sort(A, C)
            X = C.count
            X = Format(X)
            print("%06.2f" % (X), " ", end="")
        print()
            
if __name__ == "__main__":
    main()