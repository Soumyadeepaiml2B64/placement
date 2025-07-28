l = [1,2,[2,3],[4,5,6]]
for sublist in l:
    if isinstance(sublist, list):
        for item in sublist:
            print(item, end=" ") 
        print()
    else:
        print(sublist)