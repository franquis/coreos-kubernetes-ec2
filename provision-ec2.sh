#!/usr/bin/env bash
#
# Usage: ./provision-ec2-cluster.sh
#

set -e

function echo_yellow {
  echo -e "\033[0;33m$1\033[0m"
}

function echo_red {
  echo -e "\033[0;31m$1\033[0m"
}

function echo_green {
  echo -e "\033[0;32m$1\033[0m"
}

# check for EC2 API tools in $PATH
if ! which aws > /dev/null; then
  echo_red 'Please install the AWS command-line tool and ensure it is in your $PATH.'
  exit 1
fi

# check that the CoreOS user-data file is valid
# $CONTRIB_DIR/util/check-user-data.sh

# create an EC2 cloudformation stack based on CoreOS's default template
aws cloudformation create-stack \
    --template-body "$(./gen-json.py)" \
    --stack-name kubernetes \
    --parameters "$(<config.json)"

echo_green "Your Kubernetes cluster has successfully deployed to AWS CloudFormation."