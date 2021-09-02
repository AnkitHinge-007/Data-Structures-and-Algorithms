# Bubble Sort

def bubblesort(arr):
    for i in range(len(arr)):

        for j in range(0, len(arr) - i - 1):

            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


# input space separated integers
print("Enter array: ", end=" ")
arr = list(map(int,input().split(" ")))
bubblesort(arr)

print("Sorted array: ", end=" ")
for i in arr:
    print(i, end=" ")
print()
