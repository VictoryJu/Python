def foo(users):
  friends = []
  for i in range(len(users)):
    if len(users[i]) == 4:
      friends.append(users[i])
  return friends

arr = ["Ryan", "Kieran", "Mark"]
print(foo(arr))