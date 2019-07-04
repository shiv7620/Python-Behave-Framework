Feature: Login functionality

  @WebUI
  Scenario: Login with valid credentials
    Given User logs into application with "mercury" and "mercury"
    Then User logs out from application

  @WebUI
  Scenario: Login with invalid credentials
    Given User logs into application with "mercury" and "mercury12312"
    Then User logs out from application

