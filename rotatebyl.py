arr = [1,2,3,4,5,6]
def rotatebyk(arr,k):
    for i in range (k,-1,-1):
        print( arr[i])
    for i in range(k+1,len(arr)):
        print(arr[i])
rotatebyk(arr,3)