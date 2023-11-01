Feature: url shortener
  Scenario: a url can be given a shortened name
    Given I launch web browser
    When I open URL Shortener
    And I enter url "https://www.google.com"
    And I enter shorten name "GoGo"
    And I select the shorten URL button
    Then I verify url was shortened
    Then I close browser