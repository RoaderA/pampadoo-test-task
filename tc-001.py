from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import sys
from utils import close_browser
from utils import generate_vehicle_number
from utils import generate_region_code

link = "https://b2c.pampadu.ru/index.html#49a973bd-2d7c-4b9b-9c28-d986d7757983"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)
time.sleep(5)

gos_input_main = browser.find_element(By.CSS_SELECTOR, 'input[class*=gos-input-main]')
gos_input_region = browser.find_element(By.CSS_SELECTOR, 'input[class*=gos-input-region]')
continue_button = browser.find_element(By.CSS_SELECTOR, "button[class*=v-btn]")

gos_input_number = generate_vehicle_number()
gos_input_main.send_keys(gos_input_number)
gos_region_number = generate_region_code()
gos_input_region.send_keys(gos_region_number)
assert gos_input_number == gos_input_main.get_attribute('_value'), 'Значение gos_input_main не отобразилось'
assert gos_region_number == gos_input_region.get_attribute('_value'), 'значение кода региона gos_input_region не отобразилось'
print('Введенный номер отобразится в поле - passed')

continue_button.click()
time.sleep(2)
car_manufactory = browser.find_element(By.XPATH, "//label[text()='Марка автомобиля']")
assert car_manufactory.text == 'Марка автомобиля', "Номер заполнен, переход осуществлен - failed"
print ('Номер заполнен, переход осуществлен - passed')
browser.quit()