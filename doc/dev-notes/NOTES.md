# How the solution emerged...

## ⚗️ The old lab test
- create a bash script to manage the installation workflow (only OSX!)
- each step is a separate shell script
- at the end of the installation are executed the tests with inspec.io
- added some flags to perform only the test and to have the report in JUnit format. 

## 🔬 Spike A
0. create structure OS-based
1. install bats to test the brew installation
2. install brew and test it with bats
3. brew doctor
4. install the other pieces and test them with inspec

## 🧪 Spike B
0. create structure OS-based
1. install inspec via curl (or if the package manager - brew - is installed use it without installing it again)
2. install brew
3. brew doctor
4. install the other pieces and test them with inspec

## 🔭 The last spike to create a great product, not only a dev tool 
0. use Python to create the installer workflow and inspec to test each installation step.