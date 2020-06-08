# -*- python3/ utf-8 -*-

import time
import sys
import datetime
import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from playsound import playsound



def init_driver():
    """ Emulate the user's browser """
    ch_driver = 'chromedriver.exe'
    options = webdriver.ChromeOptions()
    #options.add_argument('headless')  # headless (browser starts without a graphical interface)
    driver = webdriver.Chrome(executable_path=ch_driver, chrome_options=options)
    return driver


def logging(message):
    now = datetime.datetime.now()
    time_up = now.isoformat()
    with open('log.txt', 'a') as file:
        file.write(f'{message}: {time_up} \n')


def login_hh():
    """ Log in """
    driver.get('https://hh.ru/applicant/resumes?from=header_new')
    time.sleep(2)
    try:
        driver.find_element(By.CLASS_NAME, "HH-AuthForm-Login").send_keys(login)
        time.sleep(1.5)
        driver.find_element(By.CLASS_NAME, "HH-AuthForm-Password").send_keys(my_password)
        time.sleep(1.5)
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        time.sleep(2)
        message = 'Log in Ok'
        logging(message)
    except TimeoutException:
        # playsound('sounds/pomogite-spasite-sos.mp3') # fun for fun (read README.md)
        message = 'Time Out'
        logging(message)
        driver.quit()
        sys.exit()


def update_time():
    """ Raise in search """
    try:
        driver.get('https://hh.ru/applicant/resumes?from=header_new')
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "button[data-qa='resume-update-button']").click()
        time.sleep(2)
        #playsound('sounds/nachinaju-dejstvovat-bez-shuma-i-pyli-po-vnov-utverzhennomu-planu.mp3')  # fun for fun (read README.md)
        message = 'CV update'
        logging(message)
    except ElementClickInterceptedException:
        #playsound('sounds/pomogite-spasite-sos.mp3') # fun for fun (read README.md)
        message = 'Element Click Intercepted Exception'
        logging(message)
        driver.quit()
        sys.exit()
    except NoSuchElementException:
        #playsound('sounds/pomogite-spasite-sos.mp3') # fun for fun (read README.md)
        message = 'No Such Element Exception'
        logging(message)
        driver.quit()
        sys.exit()


if __name__ == '__main__':
    login = input('Please, enter phone or email: ').split()
    #my_password = input('Please, enter password: ').split() # read README.md ('Command line & PyCharm')
    my_password = getpass.getpass('Please, enter password: ').split()
    driver = init_driver()
    login_hh()
    update_time()
    for i in range(100):
        time.sleep(14500)
        update_time()
    driver.quit()
