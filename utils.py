import sys
import random

def close_browser(browser):
    browser.quit()
    sys.exit()

def generate_vehicle_number():
    letters = ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х']
    first_letter = random.choice(letters)
    numbers = str(random.randint(000, 999)).zfill(3)
    second_and_third_letters = ''.join(random.choices(letters, k=2))
    car_number = f"{first_letter} {numbers} {second_and_third_letters}"
    return car_number

def generate_region_code():
    code = random.randint(1, 999)
    if code < 10:
        code = f"0{code}"
    return str(code)

def fake_generate_vehicle_number():
    letters = ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х']
    first_letter = random.choice(letters)
    numbers = str(random.randint(0, 99)).zfill(2)
    return f"{first_letter} {numbers}"

def fake_generate_region_code():
    code = random.randint(1, 9)
    return str(code)

