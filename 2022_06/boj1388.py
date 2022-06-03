import sys
from collections import deque
input  = sys.stdin.readline

N,M = map(int,input().split())

floor = [ list(input().strip()) for i in range(N)]
visited = [ [0]*M for i in range(N) ]

answer = 0 
dy = [1,-1,0,0]
dx = [0,0,1,-1]

def bfs(visited,i,j,answer):
      queue = deque()
      queue.append((i,j,answer))
      
      while queue:
            x, y, depth = queue.popleft()
            if floor[x][y] == '|':
                  for idx in range(2,4):
                        nx = x + dx[idx] 
                        if nx == N or nx == -1 :
                              break
                        if visited[nx][y] == 1:
                              break 
                        if floor[nx][y] == '|':       
                              visited[nx][y] = 1
                              queue.append((nx,y,answer))
            else:
                  for idx in range(0,2):
                        ny = y + dy[idx]
                        if  ny == M or ny == -1:
                              break
                        if visited[x][ny] == 1:
                              break
                        if floor[x][ny] == '-':
                              visited[x][ny] = 1
                              queue.append((x,ny,answer))
                        
for i in range(N):
      for j in range(M):
            if visited[i][j] == 0:
                  answer+=1
                  bfs(visited,i,j, answer)
print(answer)
            