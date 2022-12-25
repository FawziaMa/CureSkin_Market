Feature: Homepage Footer Links

  Scenario: User can access Terms
    Given User is on homepage
    When User scrolls down to footer
    And Clicks "Terms of service"
   Then Verify Terms of service page opened




