Stack_MAX = 10

class Stack:
    
    def __init__(self):
        self.stack = []
    
    def show(self):
        print('현재 내용물은',end='')
        print(self.stack)
    
    def push(self,num):
        if len(self.stack) != Stack_MAX:
            self.stack.append(num)
        else:
            print('Stack Over Flow')
        #print(num,'push')
    
    def pop(self):
        if len(self.stack) != 0:
            self.stack.pop()
        else:
            print("Is Empty")
        #print(num,'pop')
    
s = Stack()

while(True):
    choice = input('선택하세여: ')

    if(choice=='pop'):
        s.pop()
        s.show()

    elif(choice=='push'):
        add = input('Insert: ')
        s.push(add)
        #print('현재 내용물입니다: {0}'.format(s.show()))
    elif(choice=='end'):
        break

s.show()