m, n = map(int, input().split())

arr = [0 for _ in range(m)]
answer = 0

for i in range(m):
    arr[i]=list(map(int, input().split()))


for i in range(m):
    if answer < min(arr[i]):
        answer = min(arr[i])

print(answer)
