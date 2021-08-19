# Insertion sort

def insertionsort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j] :
            array[j+1] = array[j]
            j -= 1
        
        array[j+1] = key

# input space separated integers
print("Enter array: ", end=" ")
arr = list(map(int,input().split(" ")))
insertionsort(arr)

print("Sorted array: ", end=" ")
for i in arr:
    print(i, end=" ")
print()
