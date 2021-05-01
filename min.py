def foo(ids):
    ids.sort()
    arrlen = ids[-1]
    for i in range(0,arrlen+1):
        if i not in ids:
            arrMin = i
            return arrMin
    arrMin = arrlen + 1
    return arrMin

arr = [0,1,1,3,4]
result = foo(arr)

print(result)