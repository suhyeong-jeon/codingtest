n, k = map(int, input().split())
count = 0

while(n != 1):
    if(n%k != 0):
        n = n - 1
        count = count + 1
    else:
        n = n//k
        count = count + 1
        
print(count)
