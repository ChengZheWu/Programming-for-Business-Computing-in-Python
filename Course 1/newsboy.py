c = int(input())
r = int(input())
N = int(input())
s = int(input())
all_p = []

for i in range(N + 1):
    p = float(input())
    if 0 <= p <= 1:
        all_p.append(p)
    else:
        print("p要在0~1之間")
        break
        
if 1 <= c <= 100 and 1 <= r <= 100 and r >= c and 1 <= N <= 1000:
    best_profit = 0
    best_q = 0
    for q in range(N + 1): # 訂報紙數量
        ev = 0
        sell_p = 1
        if q == 0:
            ev = 0
        else:
            for sell_num in range(q):  # 賣出數量
                ev += (r*sell_num - c*q + s*(q - sell_num))*all_p[sell_num]
                sell_p -= all_p[sell_num]
            ev += (r*(sell_num+1) - c*q)*sell_p
        if ev > best_profit:
            best_profit = ev
            best_q = q
    print(best_q, int(best_profit))
else:
    print("輸入範圍錯誤")