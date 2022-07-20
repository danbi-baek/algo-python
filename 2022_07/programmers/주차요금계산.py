def solution(fees, records):
    answer = {}
    sumTime = {}
    cars = {}
    for i in range(len(records)):
        info = records[i].split()
        time = info[0] ; car = info[1]; inout = info[2]
        if car in cars:
            if inout == 'OUT':
                cars[car][1] = time
                inTime = cars[car][0].split(':')
                outTime = cars[car][1].split(':')
                h = (int(outTime[0]) - int(inTime[0])) * 60
                m = abs(int(inTime[1]) - int(outTime[1]))
                if car not in sumTime:
                      sumTime[car] = 0
                if inTime[1] > outTime[1]:
                      sumTime[car] += h - m
                else:
                      sumTime[car] += h + m
                cars.pop(car)  
        else:
            cars[car] = [time,'23:59']
    if cars:
        for i,car in enumerate(cars):
            if car not in sumTime : sumTime[car] = 0
            inTime = cars[car][0].split(':')
            outTime = cars[car][1].split(':')
            h = (int(outTime[0]) - int(inTime[0])) * 60
            m = abs((int(inTime[1])) - int(outTime[1]))
            if int(inTime[1]) > int(outTime[1]):
                sumTime[car] += h - m
            else:
                sumTime[car] += h + m
    for i,car in enumerate(sumTime):
        if car not in answer : answer[car] = 0
        if sumTime[car] <= fees[0]:
              answer[car] = fees[1]
        else:
            tmp = sumTime[car] - fees[0]
            if tmp % fees[2] != 0: 
                answer[car] += fees[1] + (tmp//fees[2] + 1) * fees[3] 
            else :
                answer[car] += fees[1] + (tmp//fees[2]) * fees[3]
    answer = dict(sorted(answer.items()))
    return list(answer.values())