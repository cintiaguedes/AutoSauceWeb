from selenium import webdriver
from pages.login_page import LoginPage

def before_all(context):
    context.driver = webdriver.Chrome()
    context.login_page = LoginPage(context.driver)

def after_all(context):
    context.driver.quit()
