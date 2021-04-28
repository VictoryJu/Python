def foo(ids):
    arrlen = ids[-1]
    for i in range(0,arrlen+1):
        if i not in ids:
            arrMin = i
            return arrMin
    arrMin = arrlen + 1
    return arrMin

arr = [7,3,5]
arr.sort()
result = foo(arr)

print(result)