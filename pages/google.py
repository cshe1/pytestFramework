from selenium import webdriver
import pytest
import elements.googleID as el

def test_Google():
    driver = webdriver.Chrome()
    driver.get(el.google_URL)