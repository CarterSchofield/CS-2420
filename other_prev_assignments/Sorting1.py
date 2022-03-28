import random

def createRandomList(length):
    A = []
    for i in range(length):
        n = random.randint(0,length-1)
        A.append(n)
    return(A)

def bubbleSort(A):
    changed = True
    while changed == True:
        changed = False
    #one pass to right
        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                A[i],A[i+1] = A[i+1], A[i]
                changed = True

def shakerSort(A):
    changed = True
    while changed == True:
        changed = False
        #one pass to right
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                changed = True
        #one pass to left
        for i in range(len(A)-2, -1, -1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                changed = True

def countingSort(A):
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

def mergeSort(A):
    if len(A) <= 1:
        return
    #Break A into 2 halves
    mid = len(A)//2
    L = A[0:mid]
    R = A[mid:]
    #Sort the two halves
    mergeSort(L)
    mergeSort(R)
    #merge L and R back over A
    i = 0
    J = 0
    k = 0
    while i < len(L) and J < len(R):
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

def quickSort(A, low, high):
    #basecase
    if high - low <= 0:
        return
    #1 pass of quicksort
    pivot = low
    lmgT = low+1
    for i in range(low+1, high+1):
        if A[i] < A[pivot]:
            A[i], A[lmgT] = A[lmgT], A[i]
            lmgT += 1
    pivot = lmgT - 1
    A[low], A[pivot] = A[pivot], A[low]
    #Recurse
    quickSort(A, low, pivot-1)
    quickSort(A, pivot+1, high)
    
def modQuickSort(A, low, high):
    #Basecase
    if high - low <= 0:
        return
    mid = (low+high)//2
    A[low], A[mid] = A[mid], A[low]
    #1 pass of modquicksort
    pivot = low
    lmgT = low+1
    for i in range(low+1, high+1):
        if A[i] < A[pivot]:
            A[i], A[lmgT] = A[lmgT], A[i]
            lmgT += 1
    pivot = lmgT - 1
    A[low], A[pivot] = A[pivot], A[low]
    #Recurse
    modQuickSort(A, low, pivot-1)
    modQuickSort(A, pivot+1, high)
    
def main():
    
    #BubbleSort
    A = createRandomList(8)
    B = A[:]
    bubbleSort(A)
    B.sort()
    if A != B:
        print("Error in BubbleSort")
    else:
        print("BubbleSort passed")
    
    #ShakerSort
    A = createRandomList(8)
    B = A[:]
    shakerSort(A)
    B.sort()
    if A != B:
        print("Error in ShakerSort")
    else:
        print("ShakerSort passed")
        
    #CountingSort
    A = createRandomList(8)
    B = A[:]
    countingSort(A)
    B.sort()
    if A != B:
        print("Error in CountingSort")
    else:
        print("CountingSort passed")
    
    #MergeSort
    A = createRandomList(8)
    B = A[:]
    mergeSort(A)
    B.sort()
    if A != B:
        print("Error in MergeSort")
    else:
        print("MergeSort passed")
        
    #QuickSort
    A = createRandomList(8)
    B = A[:]
    quickSort(A, 0, 7)
    B.sort()
    if A != B:
        print("Error in QuickSort")
    else:
        print("QuickSort passed")
        
    #ModifiedQuickSort
    A = createRandomList(8)
    B = A[:]
    modQuickSort(A, 0, 7)
    B.sort()
    if A != B:
        print("Error in ModifiedQuickSort")
    else:
        print("Modified QuickSort passed")
    
if __name__ == "__main__":
    main()
    