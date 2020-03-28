Feature: checking negative request to service
    
    Scenario: check getting character by wrong filter
        When send request about getting character by filter with incorrect filter
        Then validate response error about wrong field
    
    Scenario: check updating not existing character
        When send request about updating character
        Then validate not existing error in response

    Scenario: check adding character with full db
        Given add five hundred characters
        When send request about adding character
        Then validate db error in response
    
    Scenario: check adding character with not all fields
        When send request about adding character with partial data
        Then validate error about partial data in response

    Scenario: check deleting not existing character
        When send request about deleting not existing character
        Then validate not existing error in response for deleting
