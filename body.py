example1 = [10,10,10,10]
example2 = [10,20,30,40]
test1 = [12, 9, 3, 12, 7, 6, 12, 9, 2, 8, 10, 4, 4, 12, 4]
test2 = [2, 7, 4, 7, 10, 12, 12, 2, 10, 9, 5, 3, 12, 5, 7]
test3 = [3, 10, 3, 3, 8, 11, 6, 8, 11, 12, 5, 5, 12, 4, 7]
test4 = [5, 7, 7, 3, 10, 6, 11, 7, 11, 2, 9, 12, 6, 8, 10]
test5 = [9, 2, 8, 4, 11, 8, 3, 10, 2, 12, 12, 9, 10, 12, 6]

def minTime(array,k):
    partitionTable = partitions(len(array),k)
    counter = sum(array)
    for partition in partitionTable:
        if partitionTime(partition,array) <= counter:
            counter = partitionTime(partition,array)
    return counter

def partition(n, k, size=0):
    if k == size:
        return [[]]
    return [item + [i] for i in range(n+1) for item in partition(n-i, k, size = size +1)]

def partitions(n,k):
    return [[n-sum(p)] + p for p in partition(n, k-1)]

def partitionTime(partition, array):
    k = len(partition)
    time = list([0]*k)
    for i in range (0,k):
        start = sum(partition[0:i])
        end = sum(partition[0:i+1])
        time[i] = sum(array[start:end])
    return max(time)

print(minTime(example1,2))
print(minTime(example2,2))
print(minTime(test1,3))
print(minTime(test2,5))
print(minTime(test3,7))
print(minTime(test4,1))
print(minTime(test5,3))