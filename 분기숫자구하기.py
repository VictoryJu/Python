def foo(month):
    x = int(month / 3)
    if month % 3 == 0:
        x -= 1
    return x

number = int(input())
result = foo(number)+1
print(f'{result}분기 입니다.')
