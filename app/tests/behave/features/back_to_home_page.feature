Feature: Back to home page after short link was created
    As a user
    I want to be able to return to home page after short link was created
    So that I can create new short link
  Scenario: Return to home page after short link was created
    Given I launch Firefox browser
    When I open URL Shortener homepage
    And I enter the https://www.youtube.com/ url
    And I enter shorten name "youtube"
    And click on Shorten URL button
    And user can see new page with short link
    And I click on the link with id "return"
    Then successfully return to the home page
