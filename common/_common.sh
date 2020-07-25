#!/usr/bin/env bash

OS="`uname`"
TEST_STATUS=""

initialize_colors_based_on_OS(){
    case $OS in
      'Linux')
        initialize_colors_linux
        ;;
      'WindowsNT')
        OS='WIN'
        echo 'WINZOZ.... we-ve to do something :)'
        ;;
      'Darwin')
        OS='Mac'
        initialize_colors_mac
        ;;
      *) ;;
    esac
}

initialize_colors_mac(){
    RED='\033[1;31m'
    GREEN='\033[1;32m'
    NORMAL='\033[0m'
}

initialize_colors_linux(){
    RED='\e[1;31m'
    GREEN='\e[32m'
    NORMAL='\e[0m'
}


print_title() {
    echo "${RED}+----------------------------------------------------+ ${NORMAL}"
    echo "${RED}|  Script to install K8S on your local environment   | ${NORMAL}"
    echo "${RED}+----------------------------------------------------+ ${NORMAL}"
}

# Standard check bash command exit code with 3 parameters to provide user fedbacks:
# $0 - ABORT the batch in case of error.
# $1 - custom error message.
# $2 - custom success message.
check_exit_code() {
  if [ $? -ne 0 ]; then
    if [ -n "$2" ]; then
      echo  "${RED}${2}${NORMAL}" #Custom error message
    else 
      echo  "${RED}Exit CODE with error. PROCESS ABORTED!${NORMAL}"
    fi
    if [ "$1" = "ABORT" ]; then
      exit 1
    fi
  else
    if [ -n "$3" ]; then
      echo  "${GREEN}${3}${NORMAL}" #Custom successful message
    fi
  fi
}

