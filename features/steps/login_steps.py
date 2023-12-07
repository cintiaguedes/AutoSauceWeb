from behave import given, when, then
from pages.login_page import LoginPage

@given('the user is on the login page')
def step_given_user_on_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open("/login")

@when('the user enters valid credentials')
def step_when_user_enters_valid_credentials(context):
    context.login_page.login("standard_user", "secret_sauce")

@when('the user enters invalid credentials')
def step_when_user_enters_invalid_credentials(context):
    context.login_page.login("locked_out_user", "invalid_password")

@when('the user leaves username and password fields empty')
def step_when_user_leaves_empty_credentials(context):
    context.login_page.login("", "")

@when('clicks the login button')
def step_when_user_clicks_login_button(context):
    pass  # The actual login button click is handled in the login_page.py

@then('the user should be logged in successfully')
def step_then_user_logged_in_successfully(context):
    # Add assertions for successful login
    assert "inventory.html" in context.driver.current_url, "Login was not successful"

@then('an error message should be displayed')
def step_then_error_message_displayed(context):
    error_message = context.login_page.get_error_message()
    assert error_message, "Error message not displayed"

@then('an error message about required fields should be displayed')
def step_then_error_message_required_fields_displayed(context):
    error_message = context.login_page.get_error_message()
    assert "Username is required" in error_message, "Expected error message not displayed"
