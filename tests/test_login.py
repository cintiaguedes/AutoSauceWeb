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
        self.assertTrue(self.login_page.is_logout_successful())  # Assuming successful login leads to logout

    def test_invalid_login(self):
        self.login_page.open("/login")
        self.login_page.login("locked_out_user", "invalid_password")
        error_message = self.login_page.get_error_message()
        self.assertEqual(error_message, "Epic sadface: Sorry, this user has been locked out.")

    def test_logout(self):
        # Assuming that the user is initially logged in
        self.login_page.open("/dashboard")  # Change to the dashboard URL or wherever the user is redirected after login
        self.login_page.logout()
        self.assertTrue(self.login_page.is_logout_successful())

    def test_empty_credentials(self):
        self.login_page.open("/login")
        self.login_page.login("", "")
        error_message = self.login_page.get_error_message()
        self.assertEqual(error_message, "Epic sadface: Username is required")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

#test_valid_login:  logs in with valid credentials and then checks if the logout is successful.

#test_logout:  assumes the user is initially logged in, navigates to a dashboard (or any authenticated page), logs out, and checks if the logout is successful.

#test_empty_credentials:  attempts to log in with empty credentials and checks if the appropriate error message is displayed.

