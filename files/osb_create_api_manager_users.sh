#!/bin/bash

set -e

SCRIPT=$(readlink -f $0)
SCRIPT_PATH=$(dirname $SCRIPT)

source ${SCRIPT_PATH}/osb_set_environment_variables.sh

create_users_and_roles() {
	${FUSION_MIDDLEWARE_HOME}/common/bin/wlst.sh \
	  -loadProperties ${SCRIPT_PATH}/../config/osb_environment.properties \
		${SCRIPT_PATH}/osb_create_api_manager_users.py
}

create_users_and_roles
