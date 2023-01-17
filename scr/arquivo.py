import pyautogui as pag
import pyperclip
import time


pag.PAUSE = 2
#1 abrir o chorme
pag.press("winleft")
pag.write("chrome")
pag.press("enter")

#3 abrir o drive
link = "https://drive.google.com/drive/u/0/folders/14oLE59U1RqyRqlBbKpsyymW-mitvbtoh"
pyperclip.copy(link)
pag.hotkey("ctrl","v")
pag.press("enter")
time.sleep(15)

#donwland do arquivo
pag.click(x=383, y=388)
pag.click(x=1165, y=158)
pag.click(x=934, y=593)

