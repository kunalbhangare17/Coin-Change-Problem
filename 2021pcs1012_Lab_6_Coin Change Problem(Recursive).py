# A Naive recursive python program to find minimum of coins
# to make a given change V

import sys


# m is size of coins array (number of different coins)
def minCoins(coins, m, V):
    # base case
    if V == 0:
        return 0

    # Initialize result
    res = sys.maxsize

    # Try every coin that has smaller value than V
    for i in range(0, m):
        if coins[i] <= V:
            sub_res = minCoins(coins, m, V - coins[i])

            # Check for INT_MAX to avoid overflow and see if
            # result can minimized
            if sub_res != sys.maxsize and sub_res + 1 < res:
                res = sub_res + 1

    return res


# Driver program to test above function
coins = []
num = int(input("Enter the total number of coins: "))

for i in range(num):
    a = int(input(f"Enter the {i}th coin: "))
    coins.append(a)

m = len(coins)
V = int(input("Enter the total Value: "))
print("Minimum coins required is", minCoins(coins, m, V))