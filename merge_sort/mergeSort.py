def mergeSort(A):
    if len(A) <= 1:
        return
    #Break A into 2 halves
    L = A[0:mid]
    R = A[mid:]
    #Sort the two halves
    mergeSort(L)
    mergeSort(R)
    #merge L and R back over A
    i = 0
    J = 0
    k = 0
    while I < len(L) and J < len(R):
        if L[I] <= R[J]:
            A[k] = L[i]
            i += 1
            K += 1
        else:
            A[k] = R[J]
            J += 1
            k += 1
    while I < len(L):
        A[k] = L[i]
        i += 1
        k += 1
    while J < len(k):
        A[k] = R[i]
        J += 1
        k += 1
    if len(L) > i:
        A [k:] = L [i:]
    else:
        A [k:] = R [i:]

