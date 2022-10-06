### test for branch

### get c
c = int(input())
if c <= 1 or c >= 100:
    print("c is out of range !!")
    exit(1)

### get r
r = int(input())
if r <= 1 or r >= 100:
    print("r is out of range !!")
    exit(1)
if r < c:
    print("r is smaller thrn c !!")
    exit(1)

### get N
N = int(input())
if N != 8:
    print("N must be 8 !!")
    exit(1)

### get q
q = int(input())

### get p[]
p = []
for i in range(N + 1):
    # p.append(float(input()))
    if (i < q  + 1):
        p.append(float(input()))
    else:
        p[q] += float(input())

exp_money = 0
for i in range(q + 1):
    exp_money += ((i * r) - q * c) * p[i]

print(exp_money)