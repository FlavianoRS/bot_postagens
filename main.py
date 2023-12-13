from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import  os
import pandas as pd
import pyautogui
import pyperclip
from urllib.parse import quote
from datetime import datetime

#Abrindo o navegador no site do WhatsApp
navegador = webdriver.Chrome()

navegador.get("https://web.whatsapp.com")

tabela = pd.read_excel("tabelas_postagens.xlsx", sheet_name="whatsapp")

#https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}

#Esperando conectar o app no navagedor
while(len(navegador.find_elements(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')) <1):
    sleep(1)


for lin, col in tabela.iterrows():
      
    arquivo = os.path.abspath(col[3])
    mensagem = str(col[2])
    pyperclip.copy(mensagem)
    if(col[0] == "grupo"):
        try:
            #Encontrando a barra de pesquisas para os contatos e pesquisando os grupos
            navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').click()
            sleep(10)
            navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(col[1])
            sleep(3)
            #Clicando no resultados da pesquisa
            navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
            sleep(5)
        except Exception as error:
            with open("ERROS.csv", "a", newline="", encoding="utf-8") as arq:
                arq.write(f"\nGrupo {col[1]} não encontrado, verifique o nome do grupo, {datetime.now()}")
            
    else:
        try:
            while(len(navegador.find_elements(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')) <1):
                sleep(1)
            navegador.get(f"https://web.whatsapp.com/send?phone={col[1]}&text={quote(mensagem)}")
            sleep(15)
            navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
            sleep(5)
        except Exception as error:
            with open("ERROS.csv", "a", newline="", encoding="utf-8") as arq:
                arq.writelines(f"\nMensagem não enviada para {col[1]}, número inválido ,{datetime.now()}")
            
            
            
    if(col[3] != "N"):
        try:
            #Enviando o arquivo desejado junto como texto
       
            navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
            sleep(4)
            navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input').send_keys(arquivo)
            sleep(5)
        
            #Usando Pyautogui para colar o texto manualmente e enviar a postagem
            pyautogui.hotkey("ctrl", "v")
            sleep(5)
            navegador.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()
            sleep(10)
            navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
            sleep(5)
        except:
            with open("ERROS.csv", "a", encoding='utf-8') as arq:
                arq.writelines(f"\nBotão não disponível para enviar arquivo, arquivo não encontrado para {col[1]}, {datetime.now()}")
    else:
        try:
            if (col[0] == "grupo"):
                pyautogui.hotkey("ctrl", "v")
                sleep(5)
                navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
                sleep(5)
            navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
            sleep(5)
        except:
            with open("ERROS.csv", "a", encoding='utf-8') as arq:
                arq.writelines(f"\nNão foi possível enviar a mensagem, tela com caixa de mensagem alerta, {datetime.now()}")

print("terminou")
pyautogui.hotkey("ctrl","w")
navegador.close()