#MinStack

'''
Rar the Cat has developed a new data structure, the MinStack!

Rar's data structure supports the following operations:

    push: pushing an integer X to the top of the stack. (0)
    pop: removes the top integer from the stack. (1)
    top: retrieves the value of the top integer on the stack. (2)
    getMin: retrieves the value of the minimum integer in the stack. (3)

There will be a total of Q queries to the data structure. Help Rar implement it.

Implementation Details:

This is a function-call question. You are to implement the following functions:

    void push(int X): push X into the stack.
    void pop(): remove the top element from the stack.
    int top(): returns (but not remove) the top element on the stack.
    int getMin(): returns (but not remove) the minimum element on the stack.

It is guaranteed that pop, top and getMin will not be called when the stack is empty.

You may access the sample grader and solution template from the Attachments tab to test your solutions. '''

stack=[]
def push(x):
    stack.append(x)
def pop():
    stack.pop()
def top():
    return stack[-1]
def getMin():
    return min(stack)
def main():
    n=int(input())

    for i in range(n):
        parts = input().split()
        cmd = int(parts[0])
        if cmd == 0:
            val = int(parts[1])
            push(val)
        elif cmd == 1:
            pop()
        elif cmd == 2:
            print(top())
        elif cmd == 3:
            print(getMin())
main()
            
    