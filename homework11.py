import time

day = 365 * 24 * 60 * 60
timecount = 0

while True:
    timecount = day - time.time()
    print('離現在跨年的時間還有', timecount, '秒')
    time.sleep(1)