from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.trivago.com.br/")

elem = driver.find_element_by_name("sQuery")
elem.clear()
elem.send_keys("Manaus")
elem.send_keys(Keys.RETURN)
time.sleep(3)
elem = driver.find_element_by_class_name("search-button__label")
elem.click()
elem = driver.find_element_by_id("mf-select-sortby")
elem.send_keys(Keys.ARROW_DOWN)
# driver.close()


