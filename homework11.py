import time

day = 365

while True:
    print('離現在跨年的時間還有', day - time.ctime([sec]))