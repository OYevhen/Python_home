from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://9gag.com/trending")
fined = driver.find_element(By.CLASS_NAME, "badge-evt")
trend_meme_url = fined.get_attribute("href")
with open("trend_meme.txt", "a") as meme_file:
    meme_file.write(f"{trend_meme_url}\n")