Feature: Select an option
    An user selects one of the options from the list printed into the 
    console from the installer.

Scenario: Select an option from the list
    Given the user is installing the dev env for K8s
    And is printed into the console a list of options
    When the user selects one of them
    Then the installer triggers the relative action.
