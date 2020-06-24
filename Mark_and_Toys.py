price = int(input())
arr = list(map(int,input().split(" ")))
count = 0

for i in sorted(arr):
    if i<=price:
        price = price - i
        count += 1
    if i>price:
        break
    if price<=0:
        break
print(count)

