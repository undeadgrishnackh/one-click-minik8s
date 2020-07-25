# Detect the platform (similar to $OSTYPE)
#!/usr/bin/env bash

OS="`uname`"
case $OS in
  'Linux')
    OS='Linux'
    echo "{$OS} is not ready yet..."; exit 1
    ;;
  'WindowsNT')
    OS='Windows'
    echo "{$OS} is not ready yet..."; exit 1
    ;;
  'Darwin') 
    OS='Mac'
    echo "{$OS}"
    cd osx
    sh ./install.sh
    ;;
  *) ;;
esac