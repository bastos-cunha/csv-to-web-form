from time import sleep
import pyautogui
import pandas as pd

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.PAUSE = 3

#abre o navegador e acessa o link indicado
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

sleep(3)

#acessa o primeiro input com a posição obtida no procura.py
pyautogui.click(x=415, y=378)
pyautogui.write("qualqueremailparateste@blablabla.com")
pyautogui.press("tab")
pyautogui.write("qualquersenha")
pyautogui.press("tab")
pyautogui.press("enter")

df = pd.read_csv("produtos.csv")

pyautogui.PAUSE = 0.2

#loop no index do dataframe e captura as informações com o nome das colunas
for linha in df.index:
    pyautogui.click(x=409, y=250)
    
    codigo = df.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    
    marca = df.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = df.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    
    categoria = df.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    
    preco = df.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    
    custo = df.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
        
    obs = df.loc[linha, "obs"]
    if str(obs).lower() != "nan":
        pyautogui.write(str(obs))
    
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(10000)