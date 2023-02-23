Feature: login to app
  Scenario: verifying user login
    Given the user install the application and the user is on login page
    When the user enter email address
    When the user enter password
    When the user tap login button
    Then the user should see login successful
