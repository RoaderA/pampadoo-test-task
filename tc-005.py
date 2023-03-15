from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "https://b2c.pampadu.ru/index.html#49a973bd-2d7c-4b9b-9c28-d986d7757983"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)
time.sleep(5)

gos_sign_link = browser.find_element(By.CSS_SELECTOR, "span[class*=gos-sign-link]")
gos_sign_link.click()
time.sleep(2)
car_manufactory = browser.find_element(By.XPATH, "//label[text()='Марка автомобиля']")
assert car_manufactory.text == "Марка автомобиля", "Осуществляется переход на следующую форму - failed"
print('Осуществляется переход на следующую форму - passed')
browser.quit()
