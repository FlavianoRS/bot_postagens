from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

nave = webdriver.Chrome()

nave.get("https://www.facebook.com")

email = ""
senha = ""

sleep(10)
nave.find_element(By.XPATH, '//*[@id="email"]').click()
nave.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
sleep(3)
nave.find_element(By.XPATH, '//*[@id="pass"]').click()
nave.find_element(By.XPATH, '//*[@id="pass"]').send_keys(senha)
sleep(3)
nave.find_element(By.XPATH, '//*[@id="pass"]').send_keys(Keys.ENTER)
sleep(4)
nave.find_element(By.XPATH, '//*[@id="mount_0_0_O8"]/div/div[1]/div/div[2]/div[4]/div/div[1]/div[1]/ul/li[5]/span/div/a/span/svg/path[2]').click()
sleep(5)
nave.find_element(By.XPATH, '//*[@id="mount_0_0_O8"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[4]/div/div[1]/div/div/div/div/div/span/div/div[2]/div/div[2]/div/a/span/span').click()
sleep(5)
nave.find_element(By.XPATH, '//*[@id="mount_0_0_O8"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[3]/div[1]/div/div[2]/a/div').click()