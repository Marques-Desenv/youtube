from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(r"C:\Users\marqu\Documents\Coding\Youtube\Files\chromedriver.exe")
driver.maximize_window()  # Maximiza a tela do navegador
driver.get(r"https://www.youtube.com/results?search_query=bodybuilding+brasil")

user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
print(user_data)
links = []
for i in user_data:
    links.append(i.get_attribute('href'))

print(len(links))

df = pd.DataFrame(columns = ['link', 'title', 'description', 'category', 'video_tag'])
