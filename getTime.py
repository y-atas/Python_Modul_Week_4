from datetime import datetime, timedelta


def datas():
    currentTime = datetime.now()
    returnTime = currentTime + timedelta(weeks=2)
    return currentTime.strftime('%d-%m-%Y %H:%M'), returnTime.strftime('%d-%m-%Y %H:%M')
