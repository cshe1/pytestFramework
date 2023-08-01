from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import elements.googleID as el
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

def setup():
    global driver
    global wait
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get(el.GOOGLE_URL)

def test_Search():
    wait.until(ec.visibility_of_element_located((By.XPATH, el.SEARCH_BAR)))
    driver.find_element(By.XPATH, el.SEARCH_BAR).send_keys(el.SEARCH_VTUBER + Keys.ENTER)
    wait.until(ec.visibility_of_element_located((By.XPATH, el.VTUBER_FIRST_RESULT)))
