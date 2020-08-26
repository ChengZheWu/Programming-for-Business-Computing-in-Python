a = int(input("base_demand = "))
b = int(input("price sensitivity = "))
c = int(input("uint cost = "))

maxProfit = 0
optimalPrice = 0
for p in range(c+1, a//b):
	profit = (a - b*p)*(p - c)
	# print(p, profit)

	if profit > maxProfit:
		maxProfit = profit
		optimalPrice = p
	else:
		break

print("optimal price = " + str(optimalPrice))
print("maxProfit profit = " + str(maxProfit))