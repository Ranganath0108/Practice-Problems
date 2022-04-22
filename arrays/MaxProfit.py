"""Best Time Sell And buy Stocks with max profit"""


def maxProfit(arr):
    mx = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            mx = max(mx, arr[j]-arr[i])
    return mx


print(maxProfit([7, 1, 5, 3, 6, 4]))
