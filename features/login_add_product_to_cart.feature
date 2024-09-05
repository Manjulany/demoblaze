Feature: Login and adding products to carts

  @login
  Scenario: Login to demoblaze and add products to the cart
    Given the user logs into demoblaze and navigates to home page
    When user clicks open the product and add each product to the cart
    Then verifies the cart for added products
    And remove some products and verify the list