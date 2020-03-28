Feature: checking functional request to service

    Scenario: check adding character
        When send request about adding character
        Then validate this character in response

    Scenario: check getting all characters
        Given send request to add new character
        When send request about getting all characters
        Then validate our character in response

    Scenario: check getting character by filter
        Given send request to add new character for filtering request
        When send request about getting character by filter
        Then validate character in response
    
    Scenario: check updating character
        Given send request to add new character for its updating
        When send request about updating character
        Then validate character with new value in fields in response
    
    Scenario: check deleting character
        Given send request to add new character for its deleting
        When send request about deleting character
        Then validate character in response when delete
