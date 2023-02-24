n, m, k = map(int, input().split())

data = list(map(int, input().split()))
count=0
answer=0

data.sort(reverse=True)

for i in range(m):
    if(count<k):
        answer = answer + data[0]
        count = count + 1
    else:
        answer = answer + data[1]
        count = 0
    print(answer)
    





