from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.qa-practice.com/elements/button/simple")
# driver.find_element(By.ID, 'submit-id-submit').click()                                    #id="submit-id-submit"  search with #
# driver.find_element(By.CLASS_NAME, 'btn-primary').click()                                 #class="btn btn-primary"
#driver.find_element(By.CSS_SELECTOR, 'input[class="btn btn-primary"]').click()             #<input class="btn btn-primary">  search with .
# driver.find_element(By.XPATH, '//input[@class="btn btn-primary"]').click()                #<input class="btn btn-primary">
# page.find_element(By.XPATH, "//div[contains(@class, 'md:text-6xl')]")                     #<div class="font-nova text-4xl font-bold md:text-6xl">Доставка бонусів</div>
# driver.find_element(By.LINK_TEXT, 'Contact').click()                                      #Contact



