n, m = map(int, input().split())
a, b, d = map(int, input().split())
ary = [0 for _ in range(n)]
count = 0
answer = 0

for i in range(n):
    ary[i] = list(map(int, input().split()))


ary[a][b] = 2


while(True):
    if(d==0):
        if(ary[a][b-1]==0):
            d=d-1
            b=b-1
            ary[a][b]=2
        else:
            d=d-1

    if(d==-1):
        d=3
    if(d==3):
        if(ary[a+1][b]==0):
            d=d-1
            a=a+1
            ary[a][b]=2
        else:
            d=d-1

    if(d==2):
        if(ary[a][b+1]==0):
            d=d-1
            b=b+1
            ary[a][b]=2
        else:
            d=d-1
    if(d==1):
        if(ary[a-1][b]==0):
            d=d-1
            a=a-1
            ary[a][b]=2
        else:
            d=d-1

    if( ((ary[a-1][b] == 1) or (ary[a-1][b] == 2)) and
        ((ary[a+1][b] == 1) or (ary[a+1][b] == 2)) and
        ((ary[a][b-1] == 1) or (ary[a][b-1] == 2)) and
        ((ary[a][b+1] == 1) or (ary[a][b+1] == 2)) ):

        if(d==0):
            if(ary[a+1][b]==1):
                break
            else:
                a=a+1
        elif(d==1):
            if(ary[a][b-1]==1):
                break
            else:
                b=b-1
        elif(d==2):
            if(ary[a-1][b]==1):
                break
            else:
                a=a-1
        elif(d==3):
            if(ary[a][b+1]==1):
                break
            else:
                b=b+1

for i in ary:
    for j in i:
        if(j==2):
            answer = answer + 1

print(answer)


