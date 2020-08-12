Feature: Select an option from the menu
    An user selects one of the options from the list printed into the 
    console from the installer.

    Scenario Outline: 🎬 Select (E)xit from the menu
        Given the user is installing the dev env for K8s
        And is printed into the console a list of options
        When the user selects the last one (EXIT)
        Then the installer triggers the relative action
        And the installation exit with code 0.
        Examples:
