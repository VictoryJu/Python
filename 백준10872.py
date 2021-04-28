import sys

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else: 
        return num * factorial(num-1)

a = int(sys.stdin.readline())
print(factorial(a))


