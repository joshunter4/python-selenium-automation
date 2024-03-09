Feature: Target.com sign in test

  Scenario: User can sign in
    Given Open Target main page
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened