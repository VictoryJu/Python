"""
push X: 정수 X를 스택에 넣는 연산이다.

pop: 스택에서 가장 위에 있는 정수를 빼고, 
그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

size: 스택에 들어있는 정수의 개수를 출력한다.

empty: 스택이 비어있으면 1, 아니면 0을 출력한다.

top: 스택의 가장 위에 있는 정수를 출력한다. 
만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

"""
import sys

class Stack:

    def __init__(self):
        self.stack = []
    
    def push(self,X):
        self.stack.append(X)

    def pop(self):
        if len(self.stack) != 0 :
            num = self.stack.pop()    
            return num
        else:
            return -1   

    def size(self):
        print(len(self.stack))
    
    def top(self):
        if len(self.stack) != 0:
            num = self.stack.pop()
            print(num)
            self.stack.append(num)
        else:
            print(-1)
    
    def empty(self):
        if len(self.stack) != 0:
            print(0)
        else:
            print(1)

    def show(self):
        print(self.stack)

s = Stack()
i=0
num = int(sys.stdin.readline())

for i in range(num):

    choice = list(map(str,sys.stdin.readline().rstrip().split(' ')))

    if choice[0] == 'top':
        s.top()
    elif choice[0] == 'empty':
        s.empty()
    elif choice[0] == 'size':
        s.size()
    elif choice[0] == 'pop':
        print(s.pop())
    elif choice[0] == 'push':
        s.push(choice[1])
