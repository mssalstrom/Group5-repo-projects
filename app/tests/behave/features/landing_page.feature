Feature: landing page
  Scenario: Logo presences on URL Shortener Home page
    Given I launch web browser
    When I open URL Shortener
    Then I verify that the logo is present on page
    Then I close browser




