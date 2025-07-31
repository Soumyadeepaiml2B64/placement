def LargeSmallSum(arr):
    odd_pos =[arr[i] for i in range(1,len(arr),2)]
    even_pos = [arr[i] for i in range(0,len(arr),2)]

    odd_pos.sort()
    even_pos.sort()

    return(odd_pos[1]+even_pos[len(even_pos)-2])

arr = [2,3,4,5,6,7]
print(LargeSmallSum(arr))