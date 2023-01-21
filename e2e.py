from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import sys, os


def test_score_service(url):
    my_driver = webdriver.Chrome(executable_path="C:/chromedriver")
    my_driver.get(url)
    sleep(0.5)
    score = my_driver.find_element(By.ID, "score").text
    if 0 < int(score) < 1000:
        return True
    else:
        return False


def main_function():
    if test_score_service("http://127.0.0.1:5001/") == True:
        sys.exit(0)
    else:
        sys.exit(-1)
