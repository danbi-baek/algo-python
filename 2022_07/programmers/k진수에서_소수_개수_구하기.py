import math
def makeNum(n,k):
    num = ""
    while n > 0 :
        n,r = divmod(n,k)
        num += str(r)
    print(num[::-1])
    return num[::-1]
def solution(n, k):
    answer = 0
    num = makeNum(n,k).split('0')
    for i in range(len(num)):
        if num[i] == '' or int(num[i]) == 1: continue
        isPrime = True
        for j in range(2,int(math.sqrt(int(num[i])+1))):
            if (int(num[j])) % j == 0:
                isPrime = False
                break
        if isPrime: answer+=1        
                
    # for i in range(len(num)):
    #     tmp += str(num[i])
    #     print(tmp)
    #     print('tmp ' , int(tmp,k))
    # print(priNum)
    return answer

print(solution(36,3))
# 소수 : 1보다 큰 정수 1과 자기자신만으로 나누어지는수 
# 10진수 -> n진수로 변환
# 1) 10진수를 n으로 계속 나누며
# 2) 몫이 0이 될때까지 나머지를 구하고 (파이썬에서 divmod() - 몫과 나머지를 함께 반환)
# 3) 구한 나머지들을 아래서부터 취하는 방식

#리스트에서 원하는 부분을 추출(슬라이싱하기)
# [:] 콜론 앞 숫자 : 시작 인덱스, 콜론 뒷 숫자 : 추출끝나는 인덱스 + 1 
# [:] 처음부터 끝까지
# [start:] start오프셋(인덱스)부터 끝까지
# [:end] 처음부터 end-1 오프셋(인덱스)까지 
# [start : end] start오프셋부터 end-1 오프셋(인덱스)까지
# [start : end : step] step만큼 문자를 건너뛰면서, 위와 동일하게 추출
