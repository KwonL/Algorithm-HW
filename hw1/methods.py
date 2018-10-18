import random

def insertionSort(alist) :
    for i in range(1, len(alist)) :
        tmp = alist[i] 
        position = i

        while position > 0 and alist[position - 1] > tmp :
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = tmp


def mergeSort(alist) :
    if len(alist) > 1 :
        l_half = alist[:len(alist)/2]
        r_half = alist[len(alist)/2:]
        
        # l_half
        mergeSort(l_half)
        mergeSort(r_half)

        i=0
        j=0
        k=0
        while i < len(l_half) and j < len(r_half):
            if l_half[i] < r_half[j]:
                alist[k]=l_half[i]
                i=i+1
            else:
                alist[k]=r_half[j]
                j=j+1
            k=k+1

        while i < len(l_half):
            alist[k]=l_half[i]
            i=i+1
            k=k+1

        while j < len(r_half):
            alist[k]=r_half[j]
            j=j+1
            k=k+1


def quickSort(alist) : 
    quickSort_Helper(alist, 0, len(alist) - 1)
    
def quickSort_Helper(A, p, r) :
    if (p < r) :
        q = randomized_partition(A, p, r)
        quickSort_Helper(A, p, q - 1)
        quickSort_Helper(A, q + 1, r)
    return

def partition(A, p, r) :
    pivot = A[r] 
    i = p - 1
    for j in range(p, r) :
        if A[j] <= pivot :
            i += 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
    
    tmp = A[i + 1]
    A[i + 1] = A[r] 
    A[r] = tmp

    return i + 1

def randomized_partition(A, p, r) :
    i = random.sample(range(p, r), 1)[0]
    tmp = A[r] 
    A[r] = A[i]
    A[i] = tmp

    return partition(A, p, r)

def parent(i) :
    return int(int(i) / 2)
def right(i) :
    return 2 * i + 2
def left(i) :
    return 2 * i + 1

def heapify(alist, n, i): 
    largest = i 
    l = left(i)
    r = right(i)

    if l < n and alist[i] < alist[l]: 
        largest = l
    if r < n and alist[largest] < alist[r]: 
        largest = r 
    if largest != i: 
        tmp = alist[i] 
        alist[i] = alist[largest]
        alist[largest] = tmp
        
        heapify(alist, n, largest) 

def heapSort(alist): 
    n = len(alist) 
  
    for i in range(n, -1, -1): 
        heapify(alist, n, i) 
  
    for i in range(n-1, 0, -1): 
        alist[i], alist[0] = alist[0], alist[i]
        heapify(alist, i, 0) 
