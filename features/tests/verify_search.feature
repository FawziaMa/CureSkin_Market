Feature: Search Results
  Scenario: Product Details page can be accessed from Search Results
    Given User is on homepage
    And Clicks on search icon
    And User searches for cure
    And Clicks on search icon again
    When  User clicks on a product
    Then User is taken to CureSkin Under Eye Gel page