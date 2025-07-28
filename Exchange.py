def exchange_sort(arr):
    size = len(arr)
    for i in range(size-1):
        for j in range(i+1, size):
            if arr[i] > arr[j]:
                arr[i],arr[j]= arr[j],arr[i]


arr = [30,4,6,23,7,8,35]
exchange_sort(arr)
for i in range (len(arr)):
    print (arr[i],end=" ")