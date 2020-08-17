Feature: Welcome message
    A rich text welcome message into the console.

Scenario: 🔭 Launch the installer and getting the title screen.
    Given I'm installing the dev env for K8s
    When the console print the title
    Then the installer quits.

