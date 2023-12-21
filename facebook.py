from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui
import pyperclip
import pandas as pd
import os

nave = webdriver.Chrome()

tabela = pd.read_excel("tabelas_postagens.xlsx", sheet_name=1)

nave.get("https://www.facebook.com/groups/joins/?nav_source=tab")
sleep(4)
nave.maximize_window()

email = str(tabela['Login'][0])
senha = str(tabela['Senha'][0])
grupo = str(tabela['Grupos'][7])

arquivo = os.path.abspath(tabela['Arquivo'][7])
pyperclip.copy(arquivo)

sleep(10)
#Logando no Facebook
nave.find_element(By.XPATH, '//*[@id="email"]').click()
nave.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
sleep(3)
nave.find_element(By.XPATH, '//*[@id="pass"]').click()
nave.find_element(By.XPATH, '//*[@id="pass"]').send_keys(senha)
sleep(3)
nave.find_element(By.XPATH, '//*[@id="pass"]').send_keys(Keys.ENTER)
sleep(15)
pyautogui.hotkey('esc')
print("Passou")
#Entrando no grupo selecionado
sleep(5)
nave.find_element(By.LINK_TEXT, f'{grupo}').click()
sleep(5)
#Iniciando postagem com a adição de Imagem
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
pyperclip.copy(str(tabela['Menssagem'][7]))
pyautogui.hotkey("ctrl","v")
sleep(5)
#Fazendo a postagem

