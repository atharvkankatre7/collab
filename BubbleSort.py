def bubble_sort(arr):
    for i in range(len(arr)-1,0,-51):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]


arr = [30,4,6,23,7,8,35]
bubble_sort(arr)
for i in range (len(arr)):
    print (arr[i],end=" ")