def productsmallestpair(sum,arr):
    arr.sort()
    n = len(arr)
    product = 1
    for i in range(n):
        if arr[i] < sum:
            product *= arr[i]
        else:
            break
    return product 