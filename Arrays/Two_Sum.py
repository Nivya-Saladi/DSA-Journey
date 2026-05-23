def two_sum(arr, target):
    hashmap = {}
    for i in range(len(arr)):
        diff = sum - arr[i]
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[arr[i]] = i

arr = list(map(int, input("Enter elements: ")))
sum = int(input("Enter sum: "))
print(two_sum(arr, target))
