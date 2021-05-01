def foo(str):
    count = 0
    for i in str:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count += 1
    return count

arr="aeracadabra"
print(foo(arr))