import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import *
from time import sleep
import random

service = Service(executable_path="C:\chromedriver-win64\chromedriver.exe")
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9030")
driver = webdriver.Chrome(service=service, options=options)
window_handles = driver.window_handles
driver.switch_to.window(window_handles[0])

def Enter():
    pyautogui.press('enter')

def Click(x, y):
    pyautogui.moveTo(x, y)
    sleep(1)
    pyautogui.doubleClick(x, y)
    sleep(1)

def find_element(driver : webdriver.Chrome, by, value : str) -> WebElement:
    while True:
        try:
            element = driver.find_element(by, value)
            break
        except:
            pass
        sleep(0.5)
    return element

def set_bet_amount(amount: str):
    Click(780,820)
    pyautogui.typewrite(amount)
    Enter()
    sleep(6)

def get_profit():
    profit_text = driver.find_element(By.XPATH, '//div[@class="user-money_balance base-balance"]/a/div/p').text
    profit = float(profit_text)
    print(f"current_profit: ${profit_text}")
    return profit

def click_cell(row: int):
    init_x = 750
    delta_x = 200
    x = init_x + (row - 1) * delta_x
    pyautogui.click(x,550)
    sleep(0.5)

success = 0

while True:

    prev_profit = 0
    curr_profit = get_profit()

    if success == 0:
        set_bet_amount('2')
    elif success == 1:
        set_bet_amount('2')
    elif success == 2:
        set_bet_amount('3')
    elif success == 3:
        set_bet_amount('5')
    elif success == 4:
        set_bet_amount('8' )
    elif success == 5:
        set_bet_amount('12')
    elif success == 6:
        set_bet_amount('19')
    elif success == 7:
        set_bet_amount('29')
    elif success == 8:
        set_bet_amount('44')
    elif success == 9:
        set_bet_amount('67')
    elif success == 10:
        set_bet_amount('102')

    if curr_profit > prev_profit:
        prev_profit = curr_profit
        click_cell(random.randrange(1,4))
        sleep(3)
        curr_profit = get_profit()

        if curr_profit > prev_profit:
            success = 0
        else:
            success += 1
            
    if success >= 11:
        success == 0

    sleep(3)