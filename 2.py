def max_profit(prices):
    if len(prices) <= 1:
        return 0

    min_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            profit = prices[i] - min_price
            if profit > max_profit:
                max_profit = profit

    return max_profit

# Test the function
price_length=int(input("Enter number of prices"))
prices = []
for _ in range(price_length):
    element=int(input("Enter price: "))
    prices.append(element)

profit = max_profit(prices)
print("Maximum profit:", profit)
