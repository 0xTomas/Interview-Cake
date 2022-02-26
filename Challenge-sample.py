# Scope: Write an efficient function that takes stock_prices and returns the best profit
# I could have made from one purchase and one sale of one share of Apple stock yesterday.


def get_max_val(numbers):
    max = numbers[0]
    for num in numbers[1:]:
        if num > max:
            max = num
    return max


def get_min_val(numbers):
    min = numbers[0]
    for num in numbers[1:]:
        if num < min:
            min = num
    return min


stock_prices = [10, 7, 5]

print(stock_prices.index(10))
print(stock_prices.index(7))


def get_best_profit(prices):
    if len(prices) < 2:
        print("Getting a profit requires at least two prices.")

    min_price = prices[0]
    max_profit = prices[1] - prices[0]

    for current_time in range(1, len(prices)):
        current_price = prices[current_time]
        potential_profit = current_price - min_price

        max_profit = max(max_profit, potential_profit)
        min_price = min(current_price, min_price)

    return max_profit


print(f"Stock prices: {stock_prices}")
print(f"Length of stock prices: {len(stock_prices)}")
print(get_best_profit(stock_prices))


