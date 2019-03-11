#coding:utf-8
#快速排序
def QuickSort(arr,firstIndex,lastIndex):
    if firstIndex < lastIndex:
        divIndex = func(arr,firstIndex,lastIndex)

        QuickSort(arr,firstIndex,divIndex)
        QuickSort(arr,divIndex+1,lastIndex)
    else:
        return

def func(arr,firstIndex,lastIndex):
    i = firstIndex - 1
    for j in range(firstIndex,lastIndex):
        if arr[j] <= arr[lastIndex]:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[lastIndex] = arr[lastIndex],arr[i+1]
    return i

#冒泡排序
def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return  arr

#归并排序：
def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
    return c

def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)//2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)

#选择排序
def secSort(arr):
    length = len(arr)

    for i in range(0,length-1):
        smallest = i
        for j in range(i+1,length):
            if arr[j] < arr[smallest]:
                arr[j],arr[smallest] = arr[smallest],arr[j]
    return arr

#插入排序
def insertSort(arr):
    for i in range(1,len(arr)):
        j = i-1
        key = arr[i]
        while j >= 0:
            if arr[j] > key:
                arr[j+1] = arr[j]
                arr[j] = key
            j -= 1
    return arr

#希尔排序
def shellSort(arr):
    n = len(arr)
    gap = n//2
    while gap >= 1:
        for j in range(gap,n):
            i = j
            while (i-gap) >= 0:
                if arr[i] < arr[i-gap]:
                    arr[i],arr[i-gap] = arr[i-gap],arr[i]
                    i -= gap
                else:
                    break
        gap //= 2
    return arr
#堆排序
import math, random
def print_tree(array): #打印堆排序使用

    index = 0
    depth = math.ceil(math.log2(len(array)))
    sep = '  '
    for i in range(depth):
        offset = 2 ** i
        print(sep * (2 ** (depth - i - 1) - 1), end='')
        line = array[index:index + offset]
        for j, x in enumerate(line):
            print("{:>{}}".format(x, len(sep)), end='')
            interval = 0 if i == 0 else 2 ** (depth - i) - 1
            if j < len(line) - 1:
                print(sep * interval, end='')
        index += offset
        print()

def sift(data, low, high):
    i = low
    j = 2 * i + 1
    tmp = data[i]
    while j <= high:
        if j < high and data[j] > data[j + 1]:
            j += 1
        if tmp > data[j]:
            data[i] = data[j]
            i = j
            j = 2 * i + 1
        else:
            break
    data[i] = tmp

def sift_2(data,low,high):
    i = low
    j = 2 * i + 1
    tmp = data[i]
    while j <= high:
        if j < high and data[j] > data[j + 1]:
            j += 1
        if tmp > data[j]:
            data[j],data[i] = data[i],data[j]
            i = j
            j = 2 * i + 1
        else:
            break

def heap_sort(data):
    n = len(data)
    for i in range(n//2-1, -1, -1):
        sift_2(data, i, n-1)
    return data
#计数排序
def countSort(arr):
    n = len(arr)
    res = [None] * n
    for i in range(n):
        p = 0
        for j in range(n):
            if arr[i] > arr[j]:
                p += 1
        res[p] = arr[i]
    return res
#基数排序
def RadixSort(a):
    i = 0
    n = 1
    max_num = max(a)
    while max_num > 10 ** n:
        n += 1
    while i < n:
        bucket = {}
        for x in range(10):
            bucket.setdefault(x, [])
        for x in a:
            radix =int((x / (10**i)) % 10)
            bucket[radix].append(x)
        j = 0
        for k in range(10):
            if len(bucket[k]) != 0:
                for y in bucket[k]:
                    a[j] = y
                    j += 1
        i += 1
    return a
#基数排序2
def RadixSort2(arr):
    max_num = max(a)
    n = len(str(max_num))

    for i in range(0,n):
        bucket = {}
        for x in range(10):
            bucket.setdefault(x,[])
        for y in a:
            radix = int(y/(10 ** i)%10)
            bucket[radix].append(y)
        j = 0
        for k in range(10):
            if len(bucket[k]) != 0:
                for y in bucket[k]:
                    a[j] = y
                    j += 1
    return arr

#桶排序1
def bucket_sort(lst):
    buckets = [0] * ((max(lst) - min(lst))+1)
    for i in range(len(lst)):
        buckets[lst[i]-min(lst)] += 1
    res=[]
    for i in range(len(buckets)):
        if buckets[i] != 0:
            res += [i+min(lst)]*buckets[i]
    return res
#桶排序2
def buketSort(arr):
    buckets = max(arr) * [0]
    for i in range(arr):
        buckets[i] += 1

    res = []
    for i in range(len(buckets)):
        if buckets[i] != 0:
            res += buckets * i
    return res

if __name__ == '__main__':
    a = [4, 8, 7, 3, 9,22,10,14]
    print(RadixSort2(a))
