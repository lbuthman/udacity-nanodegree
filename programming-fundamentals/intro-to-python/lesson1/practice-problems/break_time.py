import time
import webbrowser

total_breaks = 3
break_count = 0

print(time.ctime())

while break_count < total_breaks:
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=Td9avGHjm8U")
    break_count += 1
