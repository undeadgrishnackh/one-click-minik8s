# 🗒️ + ✏️ Refactor I
After the local quality gates are done as well as the CI/CD implemented with CircleCI, it's time to refactor all the code to get back in shape the code quality metrics after all these spikes I've done to figure out how to handle the console, the inputs and the external process testing simulating the user interacting with it into a subprocess handled from the BDD scenarios.

So let's start:  ✅ 🛠️ 🚧 🚨

 - ✅ installer.py 
    - ✅ Unit: component creation and use
        - ✅ assert it has a menu
        - ✅ assert it has a console
        - ✅ assert it prints the welcome message
        - ✅ assert it prints the menu
        - ✅ assert it asks the questions
        - ✅ assert it receives the wrong reply
        - ✅ assert it receives the right reply
        - ✅ assert it perform the action requested
    - 🛠️ BDD: user exec it via the installer_minik8s.
        - ✅ assert it's a process
        - ✅ assert it prints the welcome message
        - ✅ assert the process was killed
        
- installer_menu.py
    - BDD: E2E tests to check the installer behaviours from an user perspective. Due to the
      system boundaries only EXIT can be tested without mocks/doubles. The others have to be
      tested with fake doubles to simulate happy (and maybe error - TBD) paths. 
        1. user exec installer_minik8s and after the title select action: EXIT (no doubles)
        1. user exec installer_minik8s and after the title select action: CHECK (fake doubles)
        1. user exec installer_minik8s and after the title select action: TEST (fake doubles)
        1. user exec installer_minik8s and after the title select action: INSTALL (fake doubles)
    - Unit:
        - assert the question
        - assert the 4 options
        - assert the 4 actions related to every option
        - assert the user input with a STUB (Exit simulation)

- installer_title.py
    - Unit:
        - assert has a console
        - assert the message
        - assert the print message behaviour
        
- menu_elements.exit
    - unit:
        - assert extend PerformAnActionInterface (informal interfaces style)
        - assert overrides perform_the_action interface with DUMMY action exit