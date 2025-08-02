#Parenthesis Matching
'''
Given an input of string in combinations of characters '{' and '}', which are parenthesis, you have to find if the input is balanced or not. The input is balanced if all the opening curly braces are closed. You can't close a curly brace before it is opened.

Input Format

Read a string from the console

Constraints

NA

Output Format

If the input is balanced print "Matching" on the console, else print "Not Matching". '''

match={')':'(','}':'{',']':'['}
s=str(input())
stack=[]
flag=0

for i in s:
    if i in match.values():
        stack.append(i)
    elif i in match:
        if not stack or stack[-1]!=match[i]:
            flag=1
            break
        stack.pop()
if flag==0 and not stack:
    print("Matching")
else:
    print("Not Matching")
