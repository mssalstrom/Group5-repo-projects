Feature: Reset URL List
  As a user
  I want to reset the URL list
  So that I can start with a clean list of shortened URLs

  Scenario: User resets the URL list
    Given I am on the URL Shortener page
    When I check if the "Reset URL List" button exists
    And I click the "Reset URL List" button
    Then the URL list should be cleared
