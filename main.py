# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import  os
import pandas as pd
import pyautogui
import pyperclip

#Abrindo o navegador no site do WhatsApp
navegador = webdriver.Chrome()

navegador.get("https://web.whatsapp.com")

arquivo = os.path.abspath("Imagens/Imagem_divulgacao_whatsapp.jpg")
mensagem = "Problemas com o seu computador, notebook ou celular? Imagine nunca mais perder horas preciosas por conta de um equipamento com defeito. Com os nossos serviços de reparo, você terá a tranquilidade de saber que seus dispositivos serão consertados de forma rápida e eficiente, permitindo que você volte a aproveitar todas as suas funcionalidades sem preocupações."
pyperclip.copy(mensagem)

#Esperando conectar o app no navagedor
while(len(navegador.find_elements(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')) <1):
    sleep(1)

#Encontrando a barra de pesquisas para os contatos e pesquisando os grupos
navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').click()
sleep(10)
navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys("Atoagem")
sleep(5)
#Clicando no resultados da pesquisa
navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
sleep(5)
#Enviando o arquivo desejado junto como texto
navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
sleep(4)
navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input').send_keys(arquivo)
sleep(5)
#Usando Pyautogui para digitar o texto manualmente
pyautogui.hotkey("ctrl", "v")
sleep(5)
navegador.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()
sleep(10)
#navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/span/button/span').click()
#sleep(5)
#navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').click()
#sleep(10)
#navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys("INFORMATIVO N.UBERLANDIA")
#sleep(5)
#navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
#sleep(5)
