#
Luffy's First Coding Contest

'''
Luffy was participating in a coding contest which contained a total of n questions.

Luffy was bounded by two rules when answering the contest questions

    Each question was accessible to Luffy starting at a particular unit of time .
    Luffy could then spend a maximum time of k units in solving that problem after which the problem became inaccessible.
    Luffy can only do one question at a particular point of time

You are given an integer array of size n, in which the i th index denotes the time when the i th question became accessible. Luffy could then spend a maximum time of k units in order to solve this question after which it became inaccessible.

That is Luffy could solve this question between the time interval : [time[i], time[i] + k - 1] inclusive.

Print the maximum amount of time that Luffy could spend in solving the contest questions.

Input Format

    First line contains two integers n and k which denote the no of questions and time for which each question stays accessible.
    The second line contains n space separated integers which denote the time when each question became accessible.
Sample Input 1

6 2
2 3 5 1 6 3

Sample Output 1

7 '''

n, k = [int(x) for x in input().split()]
times = [int(x) for x in input().split()]

times.sort()
c = 0

for i in range(n - 1):
    if times[i + 1] - times[i] < k:
        c += times[i + 1] - times[i]
    else:
        c += k

c += k
print(c)
