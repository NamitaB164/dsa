#Buy and sellmultiple stocks

'''
Write a program that takes an array that denotes the changing prices of a stock to determine the maximum profit by buying and selling one share of the stock. You can make multiple transactions.

Input Format

Read the stock prices from the first line (seperated by commas)

Constraints

NA

Output Format

Print the maximum profit as output

Sample Input 0

310,315,275,260,270,290,230,255,250

Sample Output 0

60 '''



def maximum_profit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

# Read from stdin
import sys
input_str = sys.stdin.read().strip()
prices = list(map(int, input_str.split(",")))

print(maximum_profit(prices))