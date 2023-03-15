from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from utils import close_browser
from utils import fake_generate_vehicle_number
from utils import fake_generate_region_code

link = "https://b2c.pampadu.ru/index.html#49a973bd-2d7c-4b9b-9c28-d986d7757983"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)
time.sleep(5)

gos_input_main = browser.find_element(By.CSS_SELECTOR, 'input[class*=gos-input-main]')
gos_input_region = browser.find_element(By.CSS_SELECTOR, 'input[class*=gos-input-region]')
continue_button = browser.find_element(By.CSS_SELECTOR, "button[class*=v-btn]")
check_point = browser.find_element(By.CSS_SELECTOR, "span[class*=gos-sign-title]")

gos_input_number = fake_generate_vehicle_number()
gos_input_main.send_keys(gos_input_number)
gos_region_number = fake_generate_region_code()
gos_input_region.send_keys(gos_region_number)
assert gos_input_number == gos_input_main.get_attribute('_value'), 'Значение gos_input_main не отобразилось'
assert gos_region_number == gos_input_region.get_attribute('_value'), 'значение кода региона gos_input_region не отобразилось'
print('Введенный номер отобразится в поле - passed')

continue_button.click()
time.sleep(2)

local_mark = browser.find_element(By.CSS_SELECTOR, "button[class*=v-btn]")
assert check_point.get_attribute('_value') == local_mark.get_attribute('_value'), 'При неполном поле госномера кнопка продолжить не реагирует - failed'
print('При неполном заполнении поля "Госномер" переход не осуществляется - passed')
number_field = browser.find_element(By.CSS_SELECTOR, 'div[class*=gos-input]')
field_color = number_field.get_attribute('style') #нахожу цвет поля
assert field_color == 'background-color: rgb(254, 212, 203);', 'фон поля "Госномер" окрашивается в красный - failed'
print('фон поля "Госномер" окрашивается в красный - passed')

browser.quit()