//Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

def rotate_arr(arr, k):
    k = k % len(arr)
    arr[:] = arr[-k:] + arr[:-k]
    return arr

arr = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter k: "))
print(rotate_arr(arr,k))
