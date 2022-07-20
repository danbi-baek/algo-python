from collections import *
def solution(id_list, report, k):
    answer = [0]*len(id_list)
    #동일유저 1회로 처리(중복허용x) -> 카운터함수로 중복체크 제외
    delReport = dict(Counter(report))
    reportInfo = {} #id_dic {"유저" : [신고한 id ] }
    reportUser = []
    #반복하면서 신고한 유저 횟수 count
    for key,value in delReport.items():
        id = key.split()
        reportUser.append(id[1])
        if id[0] in reportInfo:  #{"유저" : 횟수}
            reportInfo[id[0]].append(id[1])
        else:
            reportInfo[id[0]] = [id[1]]
    reportCnt = dict(Counter(reportUser))
    for value in reportCnt:
        if reportCnt[value] >= k: #k번이상 신고된 유저
            for idx, user in enumerate(reportInfo):
                if value in reportInfo[user]:
                    answer[id_list.index(user)] += 1
    return answer