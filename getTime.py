from datetime import datetime, timedelta


def datas():
    currentTime = datetime.now()
    returnTime = currentTime + timedelta(weeks=2)
    return currentTime.strftime('%m-%d-%Y %H:%M'), returnTime.strftime('%m-%d-%Y %H:%M')
