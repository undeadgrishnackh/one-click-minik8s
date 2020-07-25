#!/usr/bin/env bash
source ../common/_common.sh
source ../common/test/common_test.sh
source steps.sh
source test/test_steps.sh

initialize_colors_based_on_OS
print_title

if [ "$1" == "-h" ]; then
  echo "Usage: `basename $0` [junit] ; junit report in results directory"
  echo "       `basename $0` -t      ; skip the install and run only the tests"
  exit 0
fi
exit 0
# Installation phase
# -------------------------------------------------------------------------------------------------
if [ "$1" == "-t" ]; then
  echo "Installation phase skipped..."
else 
  install_brew
  install_virtualBox
  install_docker
  install_kubectl
  install_minikubes
  install_helm

  install_test_framework
fi

# Test phase
# -------------------------------------------------------------------------------------------------
test_title

# Minikube initialization
test_initialize_minikube_test_environment
test_initialize_helm_test_environment
# TODO: during the initialization phase we receive this WARNING MESSAGE:
# Please note: by default, Tiller is deployed with an insecure 'allow unauthenticated users' policy.
# To prevent this, run `helm init` with the --tiller-tls-verify flag.
# For more information on securing your installation see: https://docs.helm.sh/using_helm/#securing-your-helm-installation

# Unit tests
test_unit brew $1
test_unit virtualBox $1
test_unit docker $1
test_unit kubectl $1
test_unit minikube $1
test_unit helm $1
# Integration test
test_integration IT_containers $1
# E2E tests
test_e2e helm_tomcat $1
test_e2e kubectl_nginx $1

# End
test_restore_minikube_normal_environment
provide_tests_exit_code