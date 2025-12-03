from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()   

driver.get("https://quotes.toscrape.com/js/")

time.sleep(3)  

quotes = driver.find_elements(By.CLASS_NAME, "text")
authors = driver.find_elements(By.CLASS_NAME, "author")

for q, a in zip(quotes, authors):
    print(q.text, " - ", a.text)

driver.quit()
