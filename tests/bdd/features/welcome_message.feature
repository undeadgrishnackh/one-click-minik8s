Feature: Welcome message
    A rich text welcome message into the console.

    Scenario Outline: 🎬 Launch the installer and getting the title screen.
        Given I'm installing the dev env for K8s
        When the console print the title
        Then I read it as rich text.
        Examples:
