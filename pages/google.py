from selenium import webdriver
import pytest


def test_Google():
    driver = webdriver.Chrome()
    driver.get("https://google.com")