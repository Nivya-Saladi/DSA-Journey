//Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
  
def duplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)

arr = list(map(int, input("Enter elements: ").split()))
print(duplicates(arr))
