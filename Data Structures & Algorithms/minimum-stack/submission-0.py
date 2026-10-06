"""
Our input is a list of a class and a series of functions we can do
Our output should be the resukts of the functions
Edge case: empty list

This seems like a standard OOP stack question with popping and appending, returning the top of the stack and returning the min in the stack, but lets assume we want all function to be in O(1) time, getting min of the stack is O(n) because we'd have to check through the entire list to find the minimum.
To make finding the min o(1), we can creat a second stack called min_stack that keeps the minimum of the the original stack even after passing through every element
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if  len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
