Feature: Welcome message
    A rich text welcome message into the console.

Scenario: Welcome message from an .md file
    Given I'm installing the dev env for K8s
    When the console print the welcome message    
    Then I read the render of the welcome.md file.
