import sys
input = sys.stdin.readline
N = int(input())
consulting = [ list(map(int,input().split())) for _ in range(N)]
answer = 0
def dfs(day,money):
      global answer
      if day >= N :
            if answer < money:
                  answer = money
            return
      if day+consulting[day][0] <= N:
            dfs(day+consulting[day][0], money+consulting[day][1])
      else:
            dfs(day+consulting[day][0],money)
      dfs(day+1, money) 
dfs(0,0)
print(answer)