from itertools import combinations, permutations
import sys

input = sys.stdin.readline
N = int(input())
cnt = N // 2
S = [ list(map(int,input().split())) for _ in range(N)]
member = [i for i in range(N)]
minS = 200

teams = list(combinations(member,cnt)) #나눈 팀
for i,team in enumerate(teams):
      subMember = list(set(member) - set(team))  #반대팀
      teamsS = list(permutations(team,2)) #팀안에서 능력치 구하기 위한 list
      subTeamsS = list(permutations(subMember,2)) #반대팀 능력치 구하기 위한 list
      s1=s2=0
      for j in range(len(teamsS)):  #능력치 더하기
            s1 += S[teamsS[j][0]][teamsS[j][1]]
            s2 += S[subTeamsS[j][0]][subTeamsS[j][1]]
      diffS = abs(s1-s2) #능력치 차이
      if minS > diffS:
            minS = diffS      
print(minS)