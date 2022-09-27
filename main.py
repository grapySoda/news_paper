# 進貨成本
in_c = 0
# 零售價格
in_r = 0
# 需求的可能數
in_N = 0
# 訂貨量
in_q = 0
# 期望ratio
in_p = []

in_c = int(input())
if in_c <= 1 or in_c >= 100:
    print("c is out of range !!")
    exit(1)

in_r = int(input())
if in_r <= 1 or in_r >= 100:
    print("r is out of range !!")
    exit(1)
if in_r < in_c:
    print("r is smaller thrn c !!")
    exit(1)

in_N = int(input()) + 1
if in_N != 9:
    print("N must be 8 !!")
    exit(1)

in_q = int(input())

for i in range(in_N):
    in_p.append(float(input()))

out_money = 0
for i in range(in_N):
    out_money += ((i * in_r) - abs(in_q - i) * in_c) * in_p[i]

print("out_money: ", out_money)