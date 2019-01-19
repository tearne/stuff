#!/bin/bash

# Edited from https://github.com/awslabs/aws-batch-helpers/blob/master/fetch-and-run/fetch_and_run.sh

# Copyright 2013-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the
# License. A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "LICENSE.txt" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions and
# limitations under the License.

# This script can help you download and run a script from S3 using aws-cli.
# It can also download a zip file from S3 and run a script from inside.
# See below for usage instructions.

PATH="/bin:/usr/bin:/sbin:/usr/sbin:/usr/local/bin:/usr/local/sbin"
BASENAME="${0##*/}"

export S3_JOB_DIR=${1}
USER_SCRIPT=${2}
shift 2

usage () {
  if [ "${#@}" -ne 0 ]; then
    echo "----------------"
    echo "!!! ${*}"
    echo
  fi
  cat <<ENDUSAGE
----------------
Usage:

export JOB_DIR="/some/container/volume"
${BASENAME} S3-Bucket user-script.sh [ <script arguments> ]

e.g. ${BASENAME} S3://my-bucket/my-job runScript.sh arg1 arg2
ENDUSAGE

  exit 2
}

# Standard function to print an error and exit with a failing return code
error_exit () {
  echo "!!! ${BASENAME} - ${1}" >&2
  exit 1
}

if [ -z "${JOB_DIR}" ]; then
  usage "JOB_DIR is not set, this determines the download, caching, and running dir."
fi

if [ ! -d "${JOB_DIR}" ]; then
  usage "Container requires a volume mapped to 'JOB_DIR' (${JOB_DIR})."
fi

if [ -z "${S3_JOB_DIR}" ]; then
  usage "S3 job url not supplied (first argument)."
fi

if [ -z "${USER_SCRIPT}" ]; then
  usage "Run script name not suplied (second argument)."
fi

# Check that necessary programs are available
which aws >/dev/null 2>&1 || error_exit "Unable to find AWS CLI executable."

# Fetch and run a script
fetch_and_run () {
  # Create a temporary file and download the script
  aws s3 sync "${S3_JOB_DIR}" "${JOB_DIR}" --delete || error_exit "Failed to sync S3 job dir."

  # Make the temporary file executable and run it with any given arguments
  local SCRIPT="${JOB_DIR}/${USER_SCRIPT}"
  chmod u+x "${SCRIPT}" || error_exit "Failed to chmod script: ${SCRIPT}."
  exec ${SCRIPT} "${@}" || error_exit "Failed to execute script: ${SCRIPT}."
}

fetch_and_run "${@}"
