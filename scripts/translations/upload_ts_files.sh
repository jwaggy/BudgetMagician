#!/bin/bash

set -e

CI_HOME_FOLDER=$(dirname "$(readlink -f "$0")")
readonly CI_HOME_FOLDER

source "$CI_HOME_FOLDER"/../functions.sh

crowdin.bat upload sources -c "$CI_HOME_FOLDER/crowdin.yml" --identity "/d/crowdin/crowdin.yml" --base-path "."
