n = input()
data = list(map(str, input().split()))
start = [1, 1]

moving = {'R':[1,0], 'L':[-1,0], 'U':[0,1], 'D':[0,-1]}
c=0

for i in data:
    if(i=='R' and start[1]!=n):
        start[1] = start[1] + 1
    elif(i=='L' and start[1]!=1):
        start[1] = start[1] - 1
    elif(i=='U' and start[0]!=1):
        start[0] = start[0] - 1
    elif(i=='D' and start[0]!=n):
        start[0] = start[0] + 1

print(start)
