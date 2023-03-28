#########################################################
# Author: Yunus Emre ISIKDEMIR
#
# Date: 11.10.2020
# 
# Description: Stack implementation for undo/redo action
#########################################################

# Stack implementation
class Stack:
    # initialize the stack
    def __init__(self):
        self.__py_stack = []
    
    # check is empty
    def isEmpty(self):
        return self.__py_stack == []
    
    # push an element
    def push(self, item):
        self.__py_stack.append(item)
        
    # pop the top element
    def pop(self):
        return self.__py_stack.pop()
    
    # get the top element
    def top(self):
        return self.__py_stack[len(self.__py_stack) - 1]
    
    # get the size
    def size(self):
        return len(self.__py_stack)
    
    # print the intended way
    def __str__(self):
        return "<-".join(map(lambda x: str(x), self.__py_stack))
    