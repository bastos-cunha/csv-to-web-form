from time import sleep
import pyautogui

"""aguarda 5 segundos para o usuário abrir o browser e colocar o mouse na 
posição desejada"""
sleep(5)

# para identificar a posição do mouse na tela em cima do campo input
print(pyautogui.position())