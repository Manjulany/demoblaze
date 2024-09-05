Feature: Signup

  @signup
  Scenario: signup to demoblaze as a new user
    Given clicks on the Sing up button
    When fills in the Username and Password
    Then user clicks on the Sign up button
    Then new user is created