
Feature: HW4 Target


  Scenario: Verify 5 Benefit Boxes
    Given open target circle
    When verify benefit boxes

  Scenario: Target Cart Item
    Given Open Target page
    When search for nissan gtr lego
    When add legos to cart
    Then verify legos in cart