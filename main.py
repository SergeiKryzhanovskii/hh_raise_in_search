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
    chromedriver = ('chromedriver.exe')  # путь к драйверу хром

    ''' Если требуется запуск бе UI, то нужно раскомментировать "headless" '''
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # для открытия headless-браузера
    driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
    return driver


def login_hh():
    """ Вход пользователя, данные вводятся логин и пароль вводятся после запуска"""
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
        print('Time Out', now.isoformat())
        driver.quit()
        sys.exit()


def update_time():
    """ Попытка нажатия на кнопку поднятия резюме (1 раз в 4 часа)"""
    try:
        driver.get('https://hh.ru/applicant/resumes?from=header_new')
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "button[data-qa='resume-update-button']").click()
        time.sleep(2)
        playsound('sounds/nachinaju-dejstvovat-bez-shuma-i-pyli-po-vnov-utverzhennomu-planu.mp3')
        print('session Ok')
    except ElementClickInterceptedException:
        playsound('sounds/pomogite-spasite-sos.mp3')
        print('Кнопка неактивна (ElementClickInterceptedException), возможно не прошло время ожидания.',
              now.isoformat())
        driver.quit()
        sys.exit()


if __name__ == '__main__':
    login = input('Please, enter phone or email: ').split()
    my_password = input('Please, enter password: ').split()
    now = datetime.datetime.now()
    driver = init_driver()
    login_hh()
    count = 0
    for i in range(3):
        update_time()
        count += 1
        print(f'Резюме поднято в поиске раз: {count}.', now.isoformat())
        time.sleep(14500)
    driver.quit()
