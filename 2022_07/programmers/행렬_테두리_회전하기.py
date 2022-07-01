def solution(rows, columns, queries):
      answer = []
      turnMap = [[0 for _ in range(columns)] for _ in range(rows)]
      
      cnt = 0
#rows*columns크기의, 1부터 rows*columns 까지 숫자가 한줄씩 순서대로 적힌 map만들기
      for i in range(rows): 
            for j in range(columns):
                  cnt +=1
                  turnMap[i][j] = cnt
      print(turnMap)
                  
#queries 박복하면서 회전시키기
      for query in queries:
            x1,y1,x2,y2 = query
            minAns = rows*columns
            before = turnMap[x1-1][y1-1]
#qurerise의 가로(오른쪽) -> 세로(오른쪽) -> 가로(왼쪽) -> 세로(왼쪽) 순으로 값이동
            #가로(오른쪽)
            for y in range(y1, y2):
                  minAns = min(minAns,before)
                  before , turnMap[x1-1][y] = turnMap[x1-1][y], before
            #세로(오른쪽)
            for x in range(x1,x2):
                  minAns = min(minAns,before)
                  before , turnMap[x][y2-1] = turnMap[x][y2-1], before

            #가로(왼쪽)
            for y in range(y2-2,y1-2,-1):
                  minAns = min(minAns,before)
                  before , turnMap[x2-1][y] = turnMap[x2-1][y], before
            #세로(왼쪽)
            for x in range(x2-2,x1-2,-1):
                  minAns = min(minAns,before)
                  before , turnMap[x][y1-1] = turnMap[x][y1-1], before
            answer.append(minAns)
      return answer         