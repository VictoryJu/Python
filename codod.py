customer = [[1, 1], [2, 1], [3, 1], [2, 0], [2, 1]]
K = 2

def sol(customer,K):
  answer = []
  people = []
  for i in range(len(customer)):
    if customer[i][1] == 1:
      if K != 0:
        K -= 1
        answer.append(customer[i][0])
      else:
        people.append(customer[i][0])

    elif customer[i][1] == 0:
      num = -1
      for j in people:
        num += 1
        if j == customer[i][0]:
          if K > 0:
            answer.append(people.pop(num))
          else:
            people.remove(j)

      for z in answer:
        if z == customer[i][0]:
          answer.remove(customer[i][0])
          K += 1
          if len(people)>0:
            answer.append(people.pop(0))
            K -= 1
              
  answer.sort()
  return answer

print(sol(customer,K))