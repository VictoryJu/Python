def Fibo(num):
    if num>=2:
        result = (Fibo(num-1))+(Fibo(num-2))
        return result 
    elif num == 1:
        return 1
    else:
        return 0

sum = int(input())

print(Fibo(sum))