import pyautogui as p
import time

time.sleep(3)

print(p.position())
p.click(x=1080, y=376)
p.click(x=-1550, y=12)

#Двигать мышь
p.moveTo(0,0,5) 

#Печатать
p.typewrite("hello")

#Нажать кнопку
p.press("tab")