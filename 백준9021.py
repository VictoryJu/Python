# (와 )를 구별 count로 숫자를 구별 
# (면 push )면 pop
# 빠른입출력으로 수정하면 끝
import sys

num = int(sys.stdin.readline())


for i in range(num):
    arr = []
    word = sys.stdin.readline()
    temp1 = 0
    for j in word: 
        if j == '(':
            arr.append(j)
            temp1 = temp1 +1 # 여기 처리를 어케 할 것인지
        elif j ==')':
            if temp1 > 0:
                arr.pop()
                temp1 = temp1-1
            else:
                #print("NO")
                temp1 = temp1-1
                break
                
    #if temp1-temp == 0:
    if temp1 == 0:
        print("Yes")
    else:
        print("No")
  
    #     else:
    #         if len(arr)==0:
    #             num -= 1
    #             break
    #         else:
    #             arr.pop()
    #             num+=1  

    # if num > 0 :
    #     print("NO")
    # else:
    #     if len(arr) == 0:
    #         print("YES")
    #     else:
    #         print("NO")

