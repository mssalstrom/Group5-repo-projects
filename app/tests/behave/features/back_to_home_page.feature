Feature: Back to home page
    
Scenario: Return to home page after short link was created
    Given I launch chrome browser
    When open URL Shortener Home page
    And I enter the https://www.youtube.com/ url
    And I enter shorten name "youtube"
    And click on Shorten URL button
    And user can see new page with short name
    And click on return button
    Then user must successfully redirected to the home page 
    And close browser