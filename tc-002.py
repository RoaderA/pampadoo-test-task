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

vehicle_number_main = generate_vehicle_number()
gos_region_number = generate_region_code()
gos_input_main.send_keys(vehicle_number_main)
gos_input_region.send_keys(gos_region_number)
assert vehicle_number_main == gos_input_main.get_attribute('_value'), 'значение не введено в поле vehicle_number_main'
assert  gos_region_number == gos_input_region.get_attribute('_value'), 'значение не введено в поле gos_region_number'
print('Введенный номер отобразится в поле - passed')

continue_button.click()
time.sleep(5)
car_manufactory = browser.find_element(By.XPATH, "//label[text()='Марка автомобиля']").text
assert car_manufactory == "Марка автомобиля", "Номер заполнен, переход осуществлен - failed"
print('Номер заполнен, переход осуществлен - passed')

backButton = browser.find_element(By.CSS_SELECTOR, 'button[class*=v-btn--depressed]')
backButton.click()
time.sleep(5)

gos_input_main = browser.find_element(By.CSS_SELECTOR, 'input[class*=gos-input-main]')
gos_input_main_value = gos_input_main.get_attribute('_value')
gos_input_region = browser.find_element(By.CSS_SELECTOR, 'input[class*=gos-input-region]')
gos_input_region_value = gos_input_region.get_attribute('_value')

assert gos_input_main_value == vehicle_number_main and gos_input_region_value == gos_region_number, 'Открывается предыдущая форма, в поле "Госномер" отображается введенный ранее номер ТС - failed'
print('Открывается предыдущая форма, в поле "Госномер" отображается введенный ранее номер ТС - passed')
browser.quit()