arr = [10,3,5,6,20]
def madxProduct(arr):
    if len(arr) < 3:
        return 0
    arr.sort()
    return arr[-1] * arr[-2] * arr[-3]

print(madxProduct(arr))