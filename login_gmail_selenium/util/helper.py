import math
import os
import random
import secrets
import string
from random import randint, uniform
import time
from time import sleep

import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import login_gmail_selenium.common.constant as Constant


def sleep_for(period):
    sleep(randint(period[0], period[1]))




def enter_text(driver, selector, text, button=False, by=By.CSS_SELECTOR, timeout=30, max_retries=2):
    """
    Enhanced text entry function with:
    - Explicit element waiting
    - Network resilience
    - Error recovery
    - Human-like typing patterns
    """
    for attempt in range(max_retries + 1):
        try:
            # Wait for element to be interactable with extended timeout
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((by, selector)))
            
            # # Scroll element into view
            # driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", element)
            
            # Clear existing text with retries
            for _ in range(3):
                element.clear()
                if element.get_attribute('value') == '':
                    break
                time.sleep(0.5)
            
            # Human-like typing simulation
            time.sleep(random.uniform(0.2, 1.0))  # Initial hesitation
            
            for char_index, char in enumerate(text):
                # Occasionally introduce typos (5% chance)
                if random.random() < 0.05:
                    # Type wrong character
                    typo_char = random.choice(string.ascii_lowercase)
                    element.send_keys(typo_char)
                    time.sleep(random.uniform(0.1, 0.4))
                    
                    # Correct with backspace
                    element.send_keys(Keys.BACKSPACE)
                    time.sleep(random.uniform(0.1, 0.3))
                
                # Type actual character
                element.send_keys(char)
                
                # Variable typing speed with occasional pauses
                if char_index % 5 == 0 and random.random() < 0.3:
                    # Longer pause after every 5 chars sometimes
                    time.sleep(random.uniform(0.3, 0.8))
                else:
                    time.sleep(random.uniform(0.05, 0.2))
            
            # Final action if needed
            if button:
                time.sleep(random.uniform(0.5, 1.5))  # Hesitation before submit
                element.send_keys(Keys.ENTER)
                # Wait for action to start
                time.sleep(random.uniform(0.5, 1))
            
            return True
        
        except (StaleElementReferenceException, ElementNotInteractableException):
            print(f"Element became stale/uninteractable. Retry {attempt+1}/{max_retries}")
            time.sleep(2)
            continue
            
        except Exception as e:
            print(f"Text entry failed: {type(e).__name__}")
            if attempt == max_retries:
                print(f"Critical error in text entry after {max_retries} retries")
                return False
            time.sleep(3)
    
    return False




def type_text(driver, text, xpath, custom_enter=None, paste_text=Constant.PASTE_PERCENTAGE, loading=False,
              refresh=False, script=None):
    input_keyword = None
    try:
        ensure_click(driver, xpath, refresh=refresh)

        input_keyword = ensure_find_element(driver, xpath)
        input_keyword.clear()

        if random.randrange(100) < paste_text:
            input_keyword.send_keys(text)
            sleep(uniform(.01, .25))
        else:
            for letter in text:
                input_keyword.send_keys(letter)
                sleep(uniform(.1, .4))

        # TODO: improve later with this block, search icon can be unable to find
        # if random.choice([True, False]) and (custom_enter is not None):
        #     icon = driver.find_element(By.XPATH, )
        #     ensure_click(driver, icon)
        # else:

    except NoSuchElementException:
        if script:
            def retry_with_script():
                nonlocal input_keyword
                input_keyword = driver.execute_script(script)
                sleep_for(Constant.SHORT_WAIT)
                input_keyword.clear()
                input_keyword.send_keys(text)

            execute_with_retry(driver, retry_with_script)
        else:
            # TODO: need handling, still meet this case often
            raise
    # After making sure text is already typed, if error, already raised above
    input_keyword.send_keys(Keys.ENTER)

    sleep_for(Constant.SHORT_WAIT)
    if loading:
        sleep(Constant.LOADING_TIMEOUT)


def ensure_click(driver, xpath, retry=Constant.RETRY, refresh=False, script=None):
    try:
        ensure_wait_for_element(driver, xpath)

        def click_search():
            driver.find_element(By.XPATH, xpath).click()

        execute_with_retry(driver, click_search, retry=retry, refresh=refresh)

    except NoSuchElementException:
        if script:
            sleep_for(Constant.SHORT_WAIT)

            def click_with_script():
                driver.execute_script(script)

            execute_with_retry(driver, click_with_script, retry=retry, refresh=refresh)
    sleep_for(Constant.SHORT_WAIT)


def execute_with_retry(driver, callback, error=Exception, retry=Constant.RETRY, with_result=False, refresh=False):
    for i in range(retry):
        try:
            if with_result:
                return callback()
            else:
                callback()
            break
        except error:
            if refresh:
                should_refresh = i == math.floor(retry / 2)
                if should_refresh:
                    refresh_page(driver)
            if i == retry - 1:
                raise
            sleep(Constant.SHORT_TIMEOUT)


def refresh_page(driver):
    driver.get(driver.current_url)
    sleep(Constant.TRANSITION_TIMEOUT)
    driver.refresh()
    sleep(Constant.TRANSITION_TIMEOUT)


def ensure_wait_for_element(driver, xpath):
    try:
        WebDriverWait(driver, Constant.LOADING_TIMEOUT).until(EC.visibility_of_element_located(
            (By.XPATH, xpath)))
    except TimeoutException:
        # Item might be there already but not fully loaded (i guess)
        pass


def ensure_find_element(driver, xpath):
    def get_element():
        return driver.find_element(By.XPATH, xpath)

    return execute_with_retry(driver, get_element, with_result=True)


def get_version(path='C:\Program Files\Google\Chrome\Application'):
    """

    Args:
       path: link to Chrome Application
    """
    try:
        sub_folders = [f.name for f in os.scandir(path) if f.is_dir()]
        for folder in sub_folders:
            version = folder.split('.')[0]
            if version.isnumeric():
                bit = 1
                return version
    except (Exception, ValueError):
        return 0


def create_random_password():
    letters = string.ascii_letters
    digits = string.digits
    alphabet = letters + digits
    pwd_length = Constant.PASSWORD_LENGTH
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
    return pwd
