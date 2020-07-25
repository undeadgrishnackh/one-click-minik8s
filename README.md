# one-click _mini_ 🕋 K8s
💡 The idea behind this project is to provide a 'one-click' installer as the welcome package for modern developers (Probably better to call them DevOps craftsmen/craftswomen). 

## The challenge
🤔 Why is necessary to waste a lot of time in the old fashion manual installation? 

🤔 Why is necessary to waste a pair programming session to install a new workstation?

🤔 Why have we to work across multiple pairs and all the time we must suffer the __'on my machine it's on a different location'__ pain?

🛠️ As a DevOps team we must stop this pain and waste! Is a must automate all this manual work! 

🗓️ 2017 I started to create it as a pure bash installer; more as a TDD challenge versus the terminal than due to a real tech need. 

🗓️ 2020, I was doing some study on minikube VS minishift to compare them with different drivers, when I realized that was the time to refactor it in a more maintainable way.

## The solution and why it looks like this...
The challenge behind the language to handle the installation workflow was not so easy: 
- 🔦 Bash: leaving the code in bash wasn't an option for me. I was looking to enhance the code improving the modularization, the readability and last but not least, to have a better test suite from unit to integration to full E2E. The TDD test frameworks on bash aren't so advanced, so I spiked a bit on bats but I wasn't happy about the code. It wasn't so clean as I was aiming.
- 🧗‍♂️ Nodejs: with NodeJS was easier having everything with a perfect TDD flow, but the end-user might be without NodeJS so it wasn't a suitable option. Have an installer that need to install the installer engine is kinda silly 🤡. 
- 🚀 Python: is native on OSX and Linux, and on windows it became more easy to install as well directly from the store in few clicks. But because I don't consider windows a suitable platform for development (sorry windows lover I joined the dark side 🍎) I focused only on Mac OSX with the idea to extend the project one day to Linux 🐧.

🐍 **Python** incapsulates the installation workflow using some libs to enhance the user experience:
- [Rich](https://github.com/willmcgugan/rich): rich text and beautiful formatting in the terminal.
- PyInquirer: interactive command-line user interfaces.
- PyFiglet: ASCII Text with arts fonts.

🧬 [Inspec.io](https://community.chef.io/products/chef-inspec/) provides the test framework to validate each installation step's outcome.

