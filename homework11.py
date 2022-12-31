import time

day = 365 * 24 * 60 * 60

while True:
    print('離現在跨年的時間還有', day - time.time, 秒)
    time.sleep(1)