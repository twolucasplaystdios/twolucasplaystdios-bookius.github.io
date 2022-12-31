import time
#載入資料包

timer = 0
isbreak = False
# 設定變數
# timer 為主要倒數計時
# isbreak 為迴圈的結束判斷

def timer2():
    global timer, isbreak
    try:
        timer = int(input('時間'))
        if timer == 0:
            isbreak = True
    except ValueError:
        print('錯誤')
        timer2()

def countdown():
    for i in range(timer):
        time.sleep(1)
        print(timer - i)
    print('時間到了')

while True:
    timer2()
    if isbreak == True:
        break
    countdown()