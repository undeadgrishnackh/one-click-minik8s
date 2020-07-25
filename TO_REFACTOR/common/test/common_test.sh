#!/usr/bin/env bash

test_title() {
	echo -e "${GREEN}+----------------------------------------------------+${NORMAL}"
	echo -e "${GREEN}|  TEST PHASE to check the system: UNIT + IT + E2E   |${NORMAL}"
	echo -e "${GREEN}+----------------------------------------------------+${NORMAL}"
	echo -e "${GREEN}Tests in progress, please wait... ${NORMAL}"
}

test_general() {
	local SOFTWARE="$1"
	local FOLDER="$2"
	local KIND="$3"
	local JUNIT="$4"
	echo -e "╰─> ${COLOR} ${KIND} test of ${SOFTWARE} in progress...${NORMAL}"
	if [ "${JUNIT}" = "junit" ]; then
		REPORTER_ARGUMENT="--reporter junit:./test/results/${SOFTWARE}_junit.xml"
	fi
	eval "inspec exec ${FOLDER}/${SOFTWARE}_spec.rb --show_progress=true ${REPORTER_ARGUMENT}"
	if [ $? -ne 0 ]; then
		COLOR=${RED}
		STATUS=FAILURE
		TEST_STATUS="KO"
	else
		COLOR=${GREEN}
		STATUS=SUCCESS
	fi
	echo -e "${COLOR}✔ ${KIND} test of ${SOFTWARE} installation: ${STATUS}${NORMAL}"
}

test_unit() {
	test_general $1 './test/unit' Unit $2
}

test_e2e() {
	test_general $1 "../common/test/e2e/$1" "End-to-end" $2
}

test_integration() {
	test_general $1 "../common/test/integration" "Integration" $2
}

test_initialize_minikube_test_environment() {
	minikube status | grep "minikube" | grep " Running"
	if [ $? -eq 0 ]; then
		minikube stop
		check_exit_code NOABORT "Minikube stop raised an error!" "Minikube stopped properly."
	fi

	if [ -d "~./minikube" ]; then
		mv ~/.minikube ~./minikube_BCK
		check_exit_code NOABORT "Minikube backup on ~/.minikube_BCK raised an error!" "Minikube properly backuped on ~/.minikube_BCK"
	fi

	echo -e "${GREEN}Minikube is creating the test environment... ${RED}(it'll take few minutes) ${NORMAL}"
	minikube start --memory 4096
	check_exit_code ABORT "Minikube environment creation raised a CRITICAL error! TEST ABORTED!"
}

test_initialize_helm_test_environment() {
	helm init --service-account default
	check_exit_code ABORT "Helm initialization on thest environment raise a CRITICAL error! Test will go forward to test kubectl context." "Helm is properly initialized"
}

test_restore_minikube_normal_environment() {
	minikube status | grep "minikube" | grep " Running"
	if [ $? -eq 0 ]; then
		minikube stop
		check_exit_code NOABORT "Minikube test environment stop raised an error!" "Minikube test environment stopped properly."
	fi

	minikube delete
	check_exit_code NOABORT "Minikube raised an error trying to delete the test environment!" "Minikube properly deleted the test environment."

	if [ -d "~./minikube_BCK" ]; then
		mv ~./minikube_BCK ~/.minikube
		check_exit_code NOABORT "Minikube restore ~/.minikube raised an error!" "Minikube properly restored on ~/.minikube"
	fi
}

provide_tests_exit_code() {
	if [ "${TEST_STATUS}" = "KO" ]; then
		echo -e "${RED}The test phase in ERROR!    ${NORMAL}"
		echo -e "${RED}   , ,, ,                               ${NORMAL}"
		echo -e "${RED}   | || |    ,/  _____  \.              ${NORMAL}"
		echo -e "${RED}   \_||_/    ||_/     \_||              ${NORMAL}"
		echo -e "${RED}     ||       \_| . . |_/               ${NORMAL}"
		echo -e "${RED}     ||         |  L  |     Check the   ${NORMAL}"
		echo -e "${RED}     ||         |'==='|     Results !   ${NORMAL}"
		echo -e "${RED}    |>|      ___'>  -<'___              ${NORMAL}"
		echo -e "${RED}    |>|\    /             \             ${NORMAL}"
		echo -e "${RED}    \>| \  /  ,    .    .  |            ${NORMAL}"
		echo -e "${RED}     ||  \/  /| .  |  . |  |            ${NORMAL}"
		echo -e "${RED}     ||\  ' / | ___|___ |  |     (      ${NORMAL}"
		echo -e "${RED}  (( || '--'  | _______ |  |     ))  (  ${NORMAL}"
		echo -e "${RED}(  )\|| (  )\ | - --- - | -| (  ( \  )) ${NORMAL}"
		echo -e "${RED}(\/  || ))/ ( | -- - -- |  | )) )  \((  ${NORMAL}"
		echo -e "${RED} ( ()||((( ())|         |  |( (( () )	 ${NORMAL}"
		exit 666
	else
		echo -e "${GREEN}The tests are PASSED :)   ${NORMAL}"
		echo -e "${GREEN}            _             ${NORMAL}"
		echo -e "${GREEN}           (_)            ${NORMAL}"
		echo -e "${GREEN}  ___ _ __  _  ___  _   _ ${NORMAL}"
		echo -e "${GREEN} / _ \ '_ \| |/ _ \| | | |${NORMAL}"
		echo -e "${GREEN}|  __/ | | | | (_) | |_| |${NORMAL}"
		echo -e "${GREEN} \___|_| |_| |\___/ \__, |${NORMAL}"
		echo -e "${GREEN}          _/ |       __/ |${NORMAL}"
		echo -e "${GREEN}         |__/       |___/ ${NORMAL}"
	fi
}
