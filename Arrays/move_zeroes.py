//Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
def move_zeroes(arr):
    k = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[k], arr[i] = arr[i], arr[k]
            k+=1
    return arr
arr = list(map(int, input("Enter elements: ").split()))
print(move_zeroes(arr))
