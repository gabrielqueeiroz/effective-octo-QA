from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://buscacepinter.correios.com.br/app/endereco/index.php")
elem = driver.find_element_by_name("endereco")
elem.clear()
elem.send_keys("69005-040")
elem.send_keys(Keys.RETURN)

# driver.close()