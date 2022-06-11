import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
operCnt = list(map(int,input().split()))
operList = list()
for i,op in enumerate(operCnt):
      for j in range(op):
            operList.append(i) #연산자 list

#연산할 수 있는 경우의 수 list 구하기
oper = list(permutations(operList))
operList = list(set(oper)) 

minAnswer = 100000000
maxAnswer = -100000000

for j,opList in enumerate(operList):
      resultNum = A[0]
      for t,op in enumerate(opList):
            if op == 0:
                  tmpNum = resultNum + A[t+1] 
            elif op == 1:
                  tmpNum = resultNum - A[t+1]
            elif op == 2:
                  tmpNum = resultNum * A[t+1]
            else:
                  if resultNum < 0:
                        tmpNum =  -(abs(resultNum) // A[t+1])
                  else:
                        tmpNum = resultNum // A[t+1]
            resultNum = tmpNum
      if minAnswer > resultNum:
            minAnswer = resultNum
      if maxAnswer < resultNum:
            maxAnswer = resultNum
print(maxAnswer)    
print(minAnswer)