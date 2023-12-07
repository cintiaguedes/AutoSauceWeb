# tests/test_login.py

import unittest
from selenium import webdriver
from pages.login_page import LoginPage

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)

    def test_valid_login(self):
        self.login_page.open("/login")
        self.login_page.login("standard_user", "secret_sauce")
        # Add assertions for successful login

    def test_invalid_login(self):
        self.login_page.open("/login")
        self.login_page.login("locked_out_user", "invalid_password")
        error_message = self.login_page.get_error_message()
        self.assertEqual(error_message, "Epic sadface: Sorry, this user 
has been locked out.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

