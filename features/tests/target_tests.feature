Feature: Homework Test cases for Target

  Scenario: Verify Empty Cart
    Given Open Target page
    When Cart was clicked on
    Then Cart is empty

  Scenario: Target Sign In
    Given Open Target page
    When Click sign in
    And Navigation Menu
    Then Sign In