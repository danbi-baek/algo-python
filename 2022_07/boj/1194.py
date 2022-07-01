from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
answer = -1 
mirror = []; visited = [[[0 for _ in range(64)] for _ in range(m)] for _ in range(n)];alps= []; keys = ['a','b','c','d','e','f']
start = 0
dy = [-1,0,1,0]
dx = [0,1,0,-1]

for i in range(n):
      tmp = input().rstrip()
      mirror.append(tmp)
      for j in range(m):
            if 'a' <= tmp[j] <= 'f':
                  alps.append(tmp[j])
            elif tmp[j] == '0':
                  start = (i,j)

def bfs(start):
      global visited,answer,keys,mirror
      queue = deque()
      queue.append((start, 0,0))
      visited[start[0]][start[1]][0] = 1
      
      while queue:
            d, bit, cnt = queue.popleft()
            
            if mirror[d[0]][d[1]] == '1':
                  answer = cnt 
                  break
            
            for i in range(4):
                  ny = d[0] + dy[i]
                  nx = d[1] + dx[i]
                   
                  if ny < 0 or nx < 0  or ny >= n or nx >= m or mirror[ny][nx] == '#': continue
                  if visited[ny][nx][bit] == 1 : continue
                  
                  if 'a' <= mirror[ny][nx]  <= 'f':
                        idx = keys.index(mirror[ny][nx])
                        nbit = bit | (1<< idx)
                        visited[ny][nx][nbit] = 1
                        queue.append(((ny,nx), nbit, cnt+1))
                        
                  elif 'A' <= mirror[ny][nx] <= 'F':
                        alp = ord(mirror[ny][nx]) + 32
                        if chr(alp) not in alps : continue  #문에 맞는 키가 없으면
                        idx = keys.index(chr(alp))
                        nbit = bit | (1 << idx)
                        
                        if visited[d[0]][d[1]][nbit] == 0 : continue #키를 못찾았을때
                         
                        visited[ny][nx][bit] = 1
                        queue.append(((ny,nx),bit,cnt+1))
                  else:
                        visited[ny][nx][bit] = 1
                        queue.append(((ny,nx),bit,cnt+1))             
bfs(start)
print(answer)