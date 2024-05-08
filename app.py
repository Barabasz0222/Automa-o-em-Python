import pyautogui as py
import time as tm
import pandas as pd
py.PAUSE = 1
py.hotkey('win', 's')
py.write("chrome")
py.press("enter")
py.click(x=848, y=29)
py.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
py.press("enter")
tm.sleep(3)
py.click(x=853, y=375)
py.write("lucasbarabasz@icloud.com")
py.press("tab")
py.write("*********")
py.press("tab")
py.press("enter")

tabela = pd.read_csv("produtos.csv")
print(tabela)
tm.sleep(1)


for linha in tabela.index:
    py.click(x=773, y=256)
    codigo = tabela.loc[linha, "codigo"]
    py.write(str(codigo))
    py.press("tab")
    py.write(str(tabela.loc[linha, "marca"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "tipo"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "categoria"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "preco_unitario"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "custo"]))
    py.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        py.write(str(tabela.loc[linha, "obs"]))
    py.press("tab")
    py.press("enter")
    py.scroll(5000)
