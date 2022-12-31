import time

day = 365 * 24 * 60 * 60
timecount =  day - time.time

while True:
    print('離現在跨年的時間還有', timecount, '秒')
    time.sleep(1)