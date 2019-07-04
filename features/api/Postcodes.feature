Feature: Validate post code APIs

  @API
  Scenario: Search valid post code and validate returned postcodes
    Given User searches for postal codes with text "ML2"
    And User must get list of matching valid post codes

  @API
  Scenario: Search invalid post code and validate returned postcodes
    Given User searches for postal codes with text "ML2 asasd"
    And User must get list of matching valid post codes
