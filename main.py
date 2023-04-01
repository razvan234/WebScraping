import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

destination = input('Where to next? ')

def initialize_driver():
    driver = webdriver.Chrome()
    driver.get('https://www.tripadvisor.com/')
    wait = WebDriverWait(driver, 10)
    search_bar = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Where to?"]')))
    search_bar.send_keys(destination)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(3)
    return driver

def search_hotels(destination, driver):
    hotels = driver.find_element(By.XPATH, '//*[@id="search-filters"]/ul/li[2]/a')
    hotels.click()
    time.sleep(3)
    selectedhotel = driver.find_element(By.XPATH, '//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div[2]/div')
    selectedhotel.click()
    time.sleep(3)
    

def search_attractions(destination,driver):
    hotels =  driver.find_element(By.XPATH, '//*[@id="search-filters"]/ul/li[5]/a')
    hotels.click()
    time.sleep(3)

driver = initialize_driver()
selectedhotel= search_hotels(destination, driver)
search_attractions(destination,driver)

    