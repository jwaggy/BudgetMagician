#!/bin/bash

set -e

CI_HOME_FOLDER=$(dirname "$(readlink -f "$0")")
readonly CI_HOME_FOLDER

source "$CI_HOME_FOLDER"/../functions.sh

echo "Building translations."

pyside6-lupdate -noobsolete -verbose $(find "$app_base_dir" -name "*.py" -printf "%p ") -ts "$resources_dir/translations/en_US.ts"
