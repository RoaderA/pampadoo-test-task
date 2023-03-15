from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "https://b2c.pampadu.ru/index.html#49a973bd-2d7c-4b9b-9c28-d986d7757983"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)
time.sleep(5)

check_point = browser.find_element(By.CSS_SELECTOR, "span[class*=gos-sign-title]") #проверяем, что остались на той же форме
continue_button = browser.find_element(By.CSS_SELECTOR, "button[class*=v-btn]")
continue_button.click() #Кликаю на кнопку

local_mark = browser.find_element(By.CSS_SELECTOR, "button[class*=v-btn]")
assert check_point.get_attribute('_value') == local_mark.get_attribute('_value'), 'При пустом поле госномера кнопка продолжить не реагирует - failed'
print("При пустом поле госномера кнопка продолжить не реагирует - passed")
number_field = browser.find_element(By.CSS_SELECTOR, 'div[class*=gos-input]')
field_color = number_field.get_attribute('style') #нахожу цвет поля
assert field_color == 'background-color: rgb(254, 212, 203);', 'фон поля "Госномер" окрашивается в красный - failed'
print('фон поля "Госномер" окрашивается в красный - passed')

browser.quit()
