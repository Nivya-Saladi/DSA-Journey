//You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
//Merge nums1 and nums2 into a single array sorted in non-decreasing order.
//The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

def merge_arrays(arr1, arr2, m, n):
    i = m-1
    j = n-1
    k = m+n-1

    while i>=0 and j>=0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i-=1
        else:
            arr1[k] = arr2[j]
            j-=1
        k-=1
    while j>=0:
        arr1[k] = arr2[j]
        k-=1
        j-=1
    return arr1

arr1 = list(map(int, input("Enter arr1: ").split()))
m = int(input("Enter m: "))
arr2 = list(map(int, input("Enter arr2: ").split()))
n = int(input("Enter n: "))
print(merge_arrays(arr1, arr2, m, n))
