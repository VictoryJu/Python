# 정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.

class Stack:

    def __init__(self):
        self.stack = []
    
    def push(self,x):
        self.stack.append(x)

    def pop(self):
        num = self.stack.pop()
        return num

import sys

i=0
N = int(sys.stdin.readline())
s = Stack()
Sum = 0
for i in range(N):
    zam = int(sys.stdin.readline())

    if zam != 0:
        s.push(zam)
    
    elif zam == 0:
        s.pop()

for j in range(len(s.stack)):
     Sum = Sum + s.pop()    

print(Sum)





