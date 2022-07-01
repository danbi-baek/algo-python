from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split()) 
answer =0 

house = []; curr = ()
visited=[[[0 for _ in range(32)] for _ in range(n)]for _ in range(m)] #최대물건 5 = 2^5
items=[]
dx = [0,1,0,-1]
dy = [-1,0,1,0]

for i in range(m):
      tmp = input().rstrip()
      house.append(tmp)
      for j in range(n):
            if tmp[j] == 'X':
                  items.append((i,j)) #물건의 위치리스트의 인덱스
            if tmp[j] == 'S':
                  curr = (i,j)
# 1. N*M 인 맵(house)에서 S부터 찾아서 시작 E를 만날때까지 계속 상하좌우(dx,dx list)로 움직임
def bfs(curr):
      global answer,visited,items
      queue = deque()
      
      queue.append((curr,0,0)) #S부터 시작
      visited[curr[0]][curr[1]][0] = 1 #물건0개 찾은상태에서 시작
      while queue:
            d, bit, cnt  = queue.popleft()  
            if house[d[0]][d[1]] == "E" and (bit+1) == (1 << len(items)):
                  answer = cnt
                  break
            # 상하좌우 이동
            for i in range(4):
                  ny = d[0] + dy[i]
                  nx = d[1] + dx[i]
                  
                  if nx < 0 or ny < 0 or nx >= n or ny >= m or house[ny][nx] == '#' :continue
                  if visited[ny][nx][bit] == 1 : continue
                  if house[ny][nx] == "X":
                        idx = items.index((ny,nx))
                        nbit =  bit | (1 << idx)
                        visited[ny][nx][nbit] = 1
                        queue.append(((ny,nx),nbit,cnt+1))
                  else:
                        visited[ny][nx][bit] = 1
                        queue.append(((ny,nx),bit,cnt+1))
bfs(curr)
print(answer)            