#!/usr/bin/env bash

install_test_framework () {
  echo -e "\n╰─> ${GREEN} Installing test framework - inspec${NORMAL}"
  brew cask install chef/chef/inspec
  if [ $? -ne 0 ]; then
    echo -e "╰─> ${RED}Inspec brew install in Error... make it in old hugly way${NORMAL}"
    curl https://omnitruck.chef.io/install.sh | sudo bash -s -- -P inspec
    if [ $? -ne 0 ]; then
      echo -e "╰─> ${RED}Inspec Download Error! Test phase aborted.${NORMAL}"
      exit 1
    fi
  fi
}
