import pyautogui
import time


#Usando um comando de repetição, fiz com que o código prenchesse uma planilha com valores pré-determinados e dps limpasse
# Print da planilha ⇨ (https://prnt.sc/8iHUBjDwLtgF)
# Print de como o processo funcionaria na pratica ⇨ (https://prnt.sc/Sp-fdKX5Seg6)



pyautogui.hotkey('alt','tab')
time.sleep (1)

def repetir(n):    
    pyautogui.write(n)
    pyautogui.press('right')

value = ['10','20','30','40','50','60','70','80','90']
while True:
    
    pyautogui.mouseDown(x=277, y=566)
    time.sleep(1)
    pyautogui.moveTo(x=1052, y=560)
    time.sleep(1)

    pyautogui.mouseUp()
    pyautogui.rightClick()

    time.sleep(1)

    pyautogui.moveTo(x=1116, y=459)

    time.sleep (1)

    pyautogui.click()
    time.sleep (1)

    pyautogui.mouseDown(x=277, y=200)
    pyautogui.mouseUp()
    pyautogui.click()
    for n in value:repetir(n)
