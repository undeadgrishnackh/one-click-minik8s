Feature: Select an option from the menu
    An user selects one of the options from the menu printed into the
    console as a rich text from the installer.

Scenario: 🔭 Select (E)xit from the menu
    Given the user is installing the dev env for K8s
    And is printed into the console the menu's options
    When the user selects the last one (EXIT)
    Then the installer triggers the relative action
    And the installation quit with exit code 0.
