from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui
import pyperclip
import pandas as pd
import os
from datetime import datetime

nave = webdriver.Chrome()

tabela = pd.read_excel("tabelas_postagens.xlsx", sheet_name=1)

nave.get("https://www.facebook.com/groups/joins/?nav_source=tab")
sleep(4)
nave.maximize_window()
sleep(4)
try:
    email = str(tabela['Login'][0])
    senha = str(tabela['Senha'][0])
    sleep(10)
    #Logando no Facebook
    nave.find_element(By.XPATH, '//*[@id="email"]').click()
    nave.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
    sleep(3)
    nave.find_element(By.XPATH, '//*[@id="pass"]').click()
    nave.find_element(By.XPATH, '//*[@id="pass"]').send_keys(senha)
    sleep(3)
    nave.find_element(By.XPATH, '//*[@id="pass"]').send_keys(Keys.ENTER)
except:
    with open("ERROS_Facebook.csv", "a", encoding='utf-8') as arq:
          arq.writelines(f"\nFACEBOOK ERROR, Login não realizado, {datetime.now()}")
sleep(15)
pyautogui.hotkey('esc')
print("Passou")
#Entrando no grupo selecionado
for i in range(len(tabela['Grupos'])):
    grupo = str(tabela['Grupos'][i])
    try:
        arquivo = os.path.abspath(tabela['Arquivo'][i])
    except:
        with open("ERROS_Facebook.csv", "a", encoding='utf-8') as arq:
          arq.writelines(f"\nFACEBOOK ERROR, Arquivo {i+1} não encontrado, {datetime.now()}")
    pyperclip.copy(arquivo)
    sleep(5)
    try:
        nave.find_element(By.LINK_TEXT, f'{grupo}').click()
    except:
        with open("ERROS_Facebook.csv", "a", encoding='utf-8') as arq:
            arq.writelines(f"\nFACEBOOK ERROR, Grupo '{grupo}' não encontrado, {datetime.now()}")    
    sleep(5)
    #Iniciando postagem com a adição de Imagem
    try:
        imagem = pyautogui.locateCenterOnScreen('Imagens/img_imagens.png')
        pyautogui.click(imagem[0], imagem[1])
        sleep(5)
        #Adicionando a imagem na postagem
        pyautogui.click()
        sleep(5)
        pyautogui.hotkey("ctrl", "v")
        sleep(2)
        pyautogui.hotkey("Enter")
        sleep(2)
        #Colando mensagem da divulgação
        texto = pyautogui.locateCenterOnScreen('Imagens/texto.png')
        pyautogui.click(texto[0], texto[1])
        pyperclip.copy(str(tabela['Menssagem'][i]))
        pyautogui.hotkey("ctrl","v")
        sleep(5)
        #Fazendo a postagem
        publicar = pyautogui.locateCenterOnScreen('Imagens/botao_publicar.png')
        pyautogui.click(publicar[0], publicar[1])
        sleep(20)
        #Retornando para a lista dos grupos
    except:
        with open("ERROS_Facebook.csv", "a", encoding='utf-8') as arq:
            arq.writelines(f"\nFACEBOOK ERROR, Postagem não realizada para {grupo}, {datetime.now()}")
    pyautogui.hotkey("Alt", "left")
    sleep(2)
nave.close()