from selenium import webdriver   
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.dgcs.gos.pk/udocs/#/notifications")
driver.maximize_window()

data = []

time.sleep(2)

for i in range(1,7):
    xpath = "/html/body/div/div[1]/div/div/div/div/div[2]/div[1]/div/div[" +str(i)+ "]/div[1]/div[1]/div[1]"
    th = driver.find_element(By.XPATH,xpath)
    th.txt = th.text
    df = pd.DataFrame(data)
    data.append(th.txt)
    
for o in range(1,12):
    for l in range(1,7):
        xpath_2 = "/html/body/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[" +str(o)+ "]/div[" +str(l)+ "]"
        th_2 = driver.find_element(By.XPATH,xpath_2)
        th_2.txt = th_2.text
        data.append(th_2.txt)
        xpath_link = "/html/body/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[" +str(o)+ "]/div[6]/a"
        link = driver.find_element(By.XPATH,xpath_link)
        link_ref = link.get_attribute("href")
        data.append(link_ref)
        print(data)