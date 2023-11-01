Feature: filename shortener
  # Enter feature description here

  Scenario: a file can be given a shortened name
    Given I launch web browser
    When I open URL shortener
    And I enter file "File.txt"
    And I enter shortened name "Test File"
    And I select the save file button
    Then I verify url was shortened
    Then I close browser