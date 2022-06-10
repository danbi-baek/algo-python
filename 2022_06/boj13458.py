import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
B,C = map(int,input().split())
answer = 0

for i,a in enumerate(A):
      num = a - B  #총감독관
      answer += 1
      if num > 0: 
            answer += num // C #부감독관
            if num % C != 0:
                  answer += 1
print(answer)