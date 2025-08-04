m = [[1,2,3],[3,4,5],[6,7,8]]

n = 3
total = 0
for i in range(n):
    total += m[i][i]

print(total)

spiral = []
top, bottom, left, right = 0, len(m)-1, 0, len(m[0])-1

while top <= bottom and left <= right:
    for i in range(left, right+1):
        spiral.append(m[top][i])
    top += 1
    for i in range(top, bottom+1):
        spiral.append(m[i][right])
    right -= 1
    if top <= bottom:
        for i in range(right, left-1, -1):
            spiral.append(m[bottom][i])
        bottom -= 1
    if left <= right:
        for i in range(bottom, top-1, -1):
            spiral.append(m[i][left])
        left += 1

print(spiral)

n=[1,2,3,4]
n.insert(2,69)
print(n)

m=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,3):
    for j in range(i,3):
        m[i][j],m[j][i]= m[j][i],m[i][j]

print(m)
