# Buy and Sell Stocks

'''Write a program that takes an array that denotes the daily closing prices of a stock to determine the maximum profit by buying and selling one share of the stock.

Input Format

9
310 315 275 260 270 290 230 255 250

Constraints

NA

Output Format

30'''

n=int(input())
st=list(map(int,input().split()))
buy=float('inf')
p=0
for i in st:
    if i<buy:
        buy=i
    elif i-buy>p:
        p=i-buy
print(p)