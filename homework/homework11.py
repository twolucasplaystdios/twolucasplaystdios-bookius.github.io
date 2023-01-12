import time

day = 365 * 24 * 60 * 60 + time.time()
timecount = 0

while True:
    timecount = time.time() - day
    print('離現在跨年的時間還有', timecount, '秒')
    time.sleep(1)