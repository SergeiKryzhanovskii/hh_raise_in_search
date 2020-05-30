# -*- python3/ utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from playsound import playsound
import sys
import datetime


def init_driver():
    """ Инициируется браузер через Selenium """
    ch_driver = 'chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # для открытия headless-браузера
    driver = webdriver.Chrome(executable_path=ch_driver, chrome_options=options)
    return driver


def login_hh():
    """ Вход пользователя, данные (логин и пароль) вводятся после запуска"""
    driver.get('https://hh.ru/applicant/resumes?from=header_new')
    time.sleep(2)
    try:
        driver.find_element(By.CLASS_NAME, "HH-AuthForm-Login").send_keys(login)
        time.sleep(1.5)
        driver.find_element(By.CLASS_NAME, "HH-AuthForm-Password").send_keys(my_password)
        time.sleep(1.5)
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        time.sleep(2)
    except TimeoutException:
        playsound('sounds/pomogite-spasite-sos.mp3')
        now_te = datetime.datetime.now()
        time_te = now_te.isoformat()
        with open('log.txt', 'a') as file:
            file.write(f'Time Out: {time_te} \n')
        driver.quit()
        sys.exit()


def update_time():
    """ Поднятие резюме (1 раз в 4 часа)"""
    try:
        driver.get('https://hh.ru/applicant/resumes?from=header_new')
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "button[data-qa='resume-update-button']").click()
        time.sleep(2)
        playsound('sounds/nachinaju-dejstvovat-bez-shuma-i-pyli-po-vnov-utverzhennomu-planu.mp3')
    except ElementClickInterceptedException:
        playsound('sounds/pomogite-spasite-sos.mp3')
        now = datetime.datetime.now()
        time_ec = now.isoformat()
        with open('log.txt', 'a') as file:
            file.write(f'Кнопка неактивна (ElementClickInterceptedException), {time_ec} \n')
        driver.quit()
        sys.exit()


if __name__ == '__main__':
    login = input('Please, enter phone or email: ').split()
    my_password = input('Please, enter password: ').split()
    now = datetime.datetime.now()
    count = 1
    driver = init_driver()
    login_hh()
    update_time()
    print(f'CV update: {count}.', now.isoformat())
    for i in range(100):
        time.sleep(14500)
        now = datetime.datetime.now()
        time_up = now.isoformat()
        count += 1
        with open('log.txt', 'a') as file:
            file.write(f'CV update: {count}, {time_up} \n')
    driver.quit()
