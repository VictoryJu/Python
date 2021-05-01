def foo(mid):
  if mid[0] >= mid[1]:
    if mid[1] >= mid[2]:
      pos = mid[1]
      return pos
    elif mid[0] <= mid[2]:
      pos = mid[0]
      return pos
    else:
      pos = mid[2]
      return pos
  elif mid[0] > mid[2]:
    pos = mid[0]
    return pos
  elif mid[1] > mid[2]:
    pos = mid[2]
    return pos
  else:
    pos = mid[1]
    return pos

num = [5,3,4]
print(foo(num))


