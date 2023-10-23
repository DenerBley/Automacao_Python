import pyautogui
from time import sleep 

pyautogui.click(1480,332,duration=2)
pyautogui.write("Dev")

pyautogui.click(1474,358,duration=2)
pyautogui.write("123456")

pyautogui.click(1381,383,duration=1)

with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]


        pyautogui.click(677,528,duration=0.5)
        pyautogui.write(produto)

        pyautogui.click(679,554,duration=0.5)
        pyautogui.write(quantidade)

        pyautogui.click(682,579,duration=0.5)
        pyautogui.write(preco)

        pyautogui.click(588,738,duration=0.5)
        sleep(1)





