from time import sleep
import pyautogui
import pandas as pd
import tkinter as tk
from tkinter import simpledialog

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.PAUSE = 3

#abre o navegador e acessa o link indicado
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

#acessa o primeiro input com a posição obtida no procura.py
pyautogui.click(x=415, y=378)

# Cria uma janela pop-up para entrada de login e senha
root = tk.Tk()
root.withdraw()

username = simpledialog.askstring("Login", "Digite o login")
password = simpledialog.askstring("Senha", "Digite a senha", show='*')

pyautogui.write(username)
pyautogui.press("tab")
pyautogui.write(password)
pyautogui.press("tab")
pyautogui.press("enter")

df = pd.read_csv("produtos.csv")

pyautogui.PAUSE = 0.2

#loop no index do dataframe e captura as informações com o nome das colunas
for linha in df.index:
    pyautogui.click(x=409, y=250)

    for coluna in df.columns:
        if pd.notna(df.loc[linha, coluna]):
            pyautogui.write(str(df.loc[linha, coluna]))
            pyautogui.press("tab")
    
    pyautogui.press("enter")
    pyautogui.scroll(10000)

qtd = len(df.index)
pyautogui.alert(f"{qtd} produtos cadastrados com sucesso!")