# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage  

class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    LOGOUT_BUTTON = (By.ID, "logout-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container")

    def login(self, username, password):
        # Waiting for the username input field to be visible
        username_input = self.wait_for_element_to_be_visible(self.USERNAME_INPUT)
        username_input.send_keys(username)

        # Waiting for the password input field to be visible
        password_input = self.wait_for_element_to_be_visible(self.PASSWORD_INPUT)
        password_input.send_keys(password)

        # Waiting for the login button to be clickable and then clicking it
        login_button = self.wait_for_element_to_be_clickable(self.LOGIN_BUTTON)
        login_button.click()

    def logout(self):
        # Waiting for the logout button to be clickable and then clicking it
        logout_button = self.wait_for_element_to_be_clickable(self.LOGOUT_BUTTON)
        logout_button.click()

    def is_logout_successful(self):
        # Check if the login button is visible after logout, indicating successful logout
        return self.is_element_visible(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.wait_for_element(*self.ERROR_MESSAGE).text

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
