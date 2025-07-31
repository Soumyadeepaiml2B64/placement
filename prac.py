def differenceofsum(n,m):
    sum_n = 0
    sum = 0
    for i in range(m+1):
        if(i%n==0):
            sum_n +=i
        else:
            sum +=i
    print(sum_n)
    print(sum)
    return(sum - sum_n)

print(differenceofsum(4,20))