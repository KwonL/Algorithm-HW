#!/usr/bin/python
import copy
import random
from time import clock
from methods import *

f = open("./result.txt", "w")

for i in range(2, 6) :
    print("iterating over {}".format(i))
    f.write("{}\t".format(i))
    sample_list = random.sample(range(10**(i)), 10**i)

    # this is for insertion sort
    target_list = copy.deepcopy(sample_list)
    start = clock()
    insertionSort(target_list)
    end = clock()
    print("\tInsertion sort for 10^{} = {}".format(i, end-start))
    f.write(str(end-start) + "\t")

    # this is for merge sort
    target_list = copy.deepcopy(sample_list)
    start = clock()
    mergeSort(target_list)
    end = clock()
    print("\tMerge sort for 10^{} = {}".format(i, end-start))
    f.write(str(end-start) + "\t")

    # this is for quick sort
    target_list = copy.deepcopy(sample_list)
    start = clock()
    quickSort(target_list)
    end = clock()
    print("\tQuick sort for 10^{} = {}".format(i, end-start))
    f.write(str(end-start) + "\t")

    # this is for Heap sort
    target_list = copy.deepcopy(sample_list)
    start = clock()
    heapSort(target_list)
    end = clock()
    print("\tHeap sort for 10^{} = {}".format(i, end-start))
    f.write(str(end-start) + "\t")

    f.write("\n")
