Feature: User Login

  Scenario: Valid Login
    Given the user is on the login page
    When the user enters valid credentials
    And clicks the login button
    Then the user should be logged in successfully

  Scenario: Invalid Login
    Given the user is on the login page
    When the user enters invalid credentials
    And clicks the login button
    Then an error message should be displayed

  Scenario: Empty Credentials
    Given the user is on the login page
    When the user leaves username and password fields empty
    And clicks the login button
    Then an error message about required fields should be displayed

