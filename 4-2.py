location = input()
row = int(location[1])
col = int(ord(location[0])-96)
count = 0


if(row-2>0):
    if(col-1>0):
        count = count + 1
    if(col+1<9):
        count = count + 1

if(row+2<9):
    if(col-1>0):
        count = count + 1
    if(col+1<9):
        count = count + 1

if(col-2>0):
    if(row-1>0):
        count = count + 1
    if(row+1<9):
        count = count + 1

if(col+2<9):
    if(row-1>0):
        count = count + 1
    if(row+1<9):
        count = count + 1


print(count)
    
