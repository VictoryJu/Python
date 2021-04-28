def foo(str):
    count =0
    for i in str:
        if i == 'a':
            count += 1
    return count

arr="abracadabra"
print(foo(arr))