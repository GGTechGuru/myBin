import numpy
from datetime import datetime

def rangeHiLo(rangeDays, hi1lo0, dayInfoList):

    minMaxDayInfo = []

    if rangeDays < 2:
        return []

    if (hi1lo0 == 1):
        hiLoIndex = rangeDays - 2
        sign = 1
    else:
        hiLoIndex = 0
        sign = -1

    sortedReferencePrices = []
    todaysIndex = 0
    while (todaysIndex <= rangeDays -2):
        sortedReferencePrices.append(dayInfoList[todaysIndex]['price'])
        todaysIndex += 1

    dataLen = len(dayInfoList)
    while (todaysIndex < dataLen):

        todaysPrice = dayInfoList[todaysIndex]['price']
        sortedReferencePrices.sort()
        refPrice = sortedReferencePrices[hiLoIndex]

        if ((todaysPrice - refPrice) * sign) >= 0.0:
            minMaxDayInfo.append(dayInfoList[todaysIndex])

            print("REF PRICE: ", refPrice)
            print("TODAYS PRICE: ", todaysPrice)
            print("REF LIST: ", sortedReferencePrices)
            print("\n\n")

        sortedReferencePrices.remove(dayInfoList[todaysIndex-rangeDays+1]['price'])
        sortedReferencePrices.append(todaysPrice)

        todaysIndex += 1
    #

    return minMaxDayInfo
#
    
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

extrms = rangeHiLo(3, 0, dayInfoList)

print(extrms)
