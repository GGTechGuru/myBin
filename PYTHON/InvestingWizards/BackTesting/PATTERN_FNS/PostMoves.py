import numpy
from datetime import datetime, timedelta

def postHiLo(dayZeroInfo, daysAfterList, dayInfoList):

# dayZeroInfo: { 'date':datetime, 'price':float }
# daysAfterList: [ <interval sizes in which to look for up/down moves> ]
# daysInfoList: [ list of { 'date':datetime, 'price':float } ]

# Return: List of { 'daysAfter':daysAfter, 'maxUp':maxUp, 'maxDown':maxDown, 'daysToHi':daysToHi, 'daysToLo':daysToLo}

    daysAfterHiLoList = []

    dayZero = dayZeroInfo['date']
    dayZeroPrice = dayZeroInfo['price']
    maxPrice = minPrice = dayZeroInfo['price']

    daysAfterList.sort()
    currentIndex = 0

    print(daysAfterList)
    print(dayInfoList)

    maxIndex = len(dayInfoList) - 1
    for daysAfter in daysAfterList:
        print(currentIndex)

        if maxIndex <= currentIndex:
            break

        dateTimeAfter = dayZero + timedelta(days=daysAfter)

        while dayInfoList[currentIndex]['date'] < dateTimeAfter:

            currentIndex += 1

            dayInfo = dayInfoList[currentIndex]
            thisDay = dayInfo['date']
            price = dayInfo['price']
    
            if maxPrice < price:
                maxPrice = price
                daysToHi = (thisDay - dayZero).days
                continue
            
            if minPrice > price:
                minPrice = price
                daysToLo = (thisDay - dayZero).days
                continue
        #


        maxUp = (maxPrice - dayZeroPrice) / dayZeroPrice
        maxDown = (dayZeroPrice - minPrice) / dayZeroPrice

        daysAfterHiLoList.append( { 'daysAfter':daysAfter, 'maxUp':maxUp, 'maxDown':maxDown, 'daysToHi':daysToHi, 'daysToLo':daysToLo} )
    #

    return daysAfterHiLoList
    
def DayInfoMap(date, price):
    map = {
        'date': date,
        'price': price,
    }

    return map
#

dayInfoList = []
dayInfoList.append(DayInfoMap(datetime(1960, 1, 1), 100.0))
dayInfoList.append(DayInfoMap(datetime(1960, 1, 2), 101.0))
dayInfoList.append(DayInfoMap(datetime(1960, 1, 3), 99.0))
dayInfoList.append(DayInfoMap(datetime(1960, 1, 4), 100.3))
dayInfoList.append(DayInfoMap(datetime(1960, 1, 5), 101.7))
dayInfoList.append(DayInfoMap(datetime(1960, 1, 8), 100.2))
dayInfoList.append(DayInfoMap(datetime(1960, 1, 9), 103.6))
dayInfoList.append(DayInfoMap(datetime(1960, 1, 10), 97.1))
dayInfoList.append(DayInfoMap(datetime(1960, 1, 11), 100.2))

extrms = postHiLo(dayInfoList[0], [3, 6], dayInfoList)

print(extrms)
