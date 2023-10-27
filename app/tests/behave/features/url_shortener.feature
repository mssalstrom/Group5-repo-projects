Feature: url shortener
  Scenario: a url can be given a shortened name
    Given I launch browser
    When I open URL Shortener Page
    And I Enter url "https://www.google.com"
    And I Enter shorten name "GoGo"
    And I Select the Shorten URL button
    Then Go to the /your_url page
#    Then I close browser