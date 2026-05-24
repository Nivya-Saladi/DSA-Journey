//Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

def missing_number(arr):
    n = len(arr)
    total = n*(n+1) // 2
    actual = sum(arr)

    return total - actual

arr = list(map(int, input("Enter numbers: ").split()))
print(missing_number(arr))
