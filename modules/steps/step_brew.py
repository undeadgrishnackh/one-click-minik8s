import shutil
import subprocess


class StepBrew:
    @staticmethod
    def is_brew_installed():
        if shutil.which("brew"):
            return True
        else:
            return False

    @staticmethod
    def is_xcodebuild_installed():
        if shutil.which("xcodebuild"):
            return True
        else:
            return False

    @staticmethod
    def is_ruby_installed():
        if shutil.which("ruby"):
            return True
        else:
            return False

    @staticmethod
    def is_curl_installed():
        if shutil.which("curl"):
            return True
        else:
            return False

    @staticmethod
    def install_brew():
        if StepBrew.is_brew_installed() is False:
            if StepBrew.is_xcodebuild_installed() is False:
                return "Error! The system is missing xcodebuild."

            if (
                StepBrew.is_ruby_installed() is False
                or StepBrew.is_curl_installed() is False
            ):
                return (
                    "Error! The system is missing some core components: ruby or curl."
                )

            installer = subprocess.run(
                [
                    "ruby",
                    '-e "$(curl -fsSL '
                    "https://raw.githubusercontent.com/Homebrew/install/master/install)",
                ],
                stdout=subprocess.PIPE,
                universal_newlines=True,
            )
            return installer.returncode
        return 0


# step 1: install xcodebuild:    xcode-select --install
# step 1.1: check if ruby is installed
# ruby is installed on Mac, but to install it use RBENV: https://github.com/rbenv/rbenv
# step 1.2: check if curl is installed

# step2: install brew:  ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# TODO: ruby installer is deprecated! bash is the new one! Refactor the code to use the new way of installing...
# step2 UPDATE: --> /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
