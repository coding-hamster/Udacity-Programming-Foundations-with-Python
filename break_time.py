import webbrowser
import time

a = 0
print('This program started on '+time.ctime())
while a < 3:
    time.sleep(10)
    webbrowser.open('https://www.youtube.com/watch?v=x2i5Jp7mdMc')
    a += 1