def get_max_profit(stock):
    profit = 0
    bought = []
    sold = []
    # stock.append(0)
    # i = 0
    max_current_future_price = 0
    profit = 0
    for i in xrange(len(stock)-1, -1, -1):
        max_current_future_price = max(max_current_future_price, stock[i])
        profit += (max_current_future_price - stock[i])
        
    return profit

def main():
    t = int(raw_input())
    for __ in xrange(t):
        _ = raw_input()
        print get_max_profit(map(int, raw_input().split()))

if __name__ == "__main__":
    main()