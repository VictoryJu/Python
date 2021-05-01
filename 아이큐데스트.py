def foo(numbers):
  oddCount = 0
  evenCount = 0
  arrlen = len(numbers)

  for i in range(0,arrlen):
    if oddCount == 2:
      for j in range(0,arrlen):
        if numbers[j] % 2 == 0:
          pos = j+1
          return pos

    if evenCount == 2:
      for j in range(0,arrlen):
        if numbers[j] % 2 != 0:
          pos = j+1
          return pos

    if numbers[i] % 2 != 0:
      oddCount += 1

    if numbers[i] % 2 == 0:
      evenCount += 1

arr = [1,2,2,4,6,8]
print(foo(arr))
