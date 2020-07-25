#!/usr/bin/env bash

# Installation functions
# -------------------------------------------------------------------------------------------------

install_brew() {
	echo -e "\n╰─> ${GREEN} brew - as mac package manager${NORMAL}"
	/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	check_exit_code ABORT "Something goes wrong installing brew; the batch is ABORTED!"
	# disabled to have a more smooth installation and test phase. Is up-to-the-user to take care of his machine.
	# brew update
	# brew upgrade
}

install_virtualBox() {
	echo -e "\n╰─> ${GREEN} Virtual Box last version and related extension packs${NORMAL}"
	brew cask install virtualbox
	check_exit_code NOABORT "VirtualBox installation raise an error but the script goes forward till the test phase!"
}

install_docker() {
	echo -e "\n╰─> ${GREEN} Docker and related tools and GUI${NORMAL}"
	brew cask install docker
	check_exit_code NOABORT "Docker installation raise an error but the script goes forward till the test phase!"
	brew cask install kitematic
	check_exit_code NOABORT "Kitematic installation raise an error but the script goes forward till the test phase!"
}

install_kubectl() {
	echo -e "\n╰─> ${GREEN} Kubectl${NORMAL}"
	brew install kubectl
	check_exit_code NOABORT "Kubectl installation raise an error but the script goes forward till the test phase!"
}

install_minikubes() {
	echo -e "\n╰─> ${GREEN} Minikube${NORMAL}"
	brew cask install minikube
	check_exit_code NOABORT "Minikube installation raise an error but the script goes forward till the test phase!"
}

install_helm() {
	echo -e "\n╰─> ${GREEN} K8s Helm + init${NORMAL}"
	brew install kubernetes-helm
	check_exit_code NOABORT "Helm installation raise an error but the script goes forward till the test phase!"
}