Feature: Search Results
  Scenario: Product Details page can be accesed from Search Results
    Given User is on homepage
    And Clicks on search icon
    And User searches for cure
    When  User clicks on a product
   Then User is taken to product page