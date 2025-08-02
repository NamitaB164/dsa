#Flawless Numbers

'''


    Problem
    Submissions
    Leaderboard
    Discussions

Luffy is participating in a numbers game. He is given a array of n numbers and have to find if the array of numbers is flawless.

An array of numbers is considered flawless if and only if for every pair of elements ai,aj ; i != j there exists an element ak such that ak = ai * aj. Where k can also be equal to i or j.

Find out if the given array of numbers is flawless.

Input Format

First line of the input contains an integer T denoting the number of test cases. T test cases follow.

First line of each test case contains an integer n denoting number of elements in the array.

Next line contains n space separated integers denoting the array elements.

Constraints

    1 <= T <= 10^9
    2 <= n <= 10^9
    -10^9 ≤ ai ≤ 10^9

Output Format

For each test case, output a single line containing "yes" or "no" (without quotes) corresponding to the answer of the problem

Sample Input 0

3
2
0 1
2
1 2
2
5 6

Sample Output 0

yes
yes
no '''

n=int(input())
#print(n)
for i in range(n):
    x=int(input())
    #print(x)
    lt=list(map(int,input().split()))
    #print(lt)
    s=set(lt)
    flag=0
    for i in range (x):
        for j in range(x):
            if i!=j and lt[i]*lt[j] not in s:
                flag=1
                break
    if flag==0:
        print("yes")
    else:
        print("no")

