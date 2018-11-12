#!/usr/bin/env python3

import argparse
import os
import time


def get_args():
    parser = argparse.ArgumentParser(prog='sorting_deck.py')
    parser.add_argument('--algo', default='bubble')
    parser.add_argument('--gui', action='store_true', default=False)
    parser.add_argument('N', nargs='+', default=True)
    return parser.parse_args()


# -------------bubble sort-------------
def bubble(arr):
    for i in range(len(arr)):
        swap = False
        for j in range(len(arr) - i - 1):
            if int(arr[j]) > int(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
                print(' '.join(arr))
                if get_args().gui:  # this is for GUI option
                    return arr
        if swap is False:  # stop function if the array is sorted
            break
    return arr


# -----------------insertion sort-----------------
def insert(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and int(key) < int(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        if j + 1 != i:  # prevent running when the array already sroted
            print(' '.join(arr))
            if get_args().gui:  # this is for GUI option
                return arr
    return arr


# ---------------------quick sort-----------------------
'''how quick sort work
quick sort ind a pivot from the array, then divide the array into two subarray
specified by the pivot (one are all elem that smaller than pivot and the other
is the pivot and all elem that greater than it)
then it continue to search for the pivot from the subarray until the whole
aray is sorted.
'''


def partition(arr, low, high):  # this func return the pivot pos in the array
    pivot = arr[high]
    # the pivot here is the last elem of the array (or subarray)
    print('P:', pivot)
    i = -1
    j = low  # j is the first elem of the array (or subarray)
    for j in range(high):  # in the range of the array (or subarray)
        if int(arr[j]) <= int(pivot):  # compare the pivot with arr[j]
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(' '.join(arr))
    return i + 1


def quick(arr, low, high):  # this function divide array
    if low < high:  # this mean the subarray have length > 1
        pivot = partition(arr, low, high)
        quick(arr, low, pivot - 1)
        quick(arr, pivot + 1, high)
    return arr


# -------------------merge sort-------------------
'''how merge sort work
first: it find the middle point of the array (subarray or not still have to
fine the middle point) and then split the array into subarray by that point
second: recursive the above step until there is no subarray can be divide.
last: combine by merging the two sorted subarrays back into single sorted
subarray
'''


def merge(arr):
    if len(arr) > 1:
        m = len(arr) // 2  # find the mid point of the array
        L = arr[:m]
        R = arr[m:]
        merge(L)
        merge(R)
        merge_sort(arr, L, R)
        if get_args().gui:
            return arr
    return arr


def merge_sort(arr, L, R):
    i = j = k = 0
    # ----copy data to a temp arrays
    while i < len(L) and j < len(R):
        if int(L[i]) < int(R[j]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    # ------check whether any elem left
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
    print(' '.join(arr))
    return arr


# -------------the main function--------------
def main():
    args = get_args()
    arr = args.N
    # print(args.N)
    if args.gui:
        import GUI
    elif len(args.N) >= 15 and args.gui:
        print('Input too large')
    else:
        if args.algo == 'insert':
            insert(arr)
        elif args.algo == 'quick':
            low = 0
            high = len(arr) - 1
            quick(arr, low, high)
        elif args.algo == 'merge':
            merge(arr)
        else:
            bubble(arr)
    return arr


if __name__ == '__main__':
    main()
