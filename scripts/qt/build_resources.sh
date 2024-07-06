#!/bin/bash

set -e

CI_HOME_FOLDER=$(dirname "$(readlink -f "$0")")
readonly CI_HOME_FOLDER

source "$CI_HOME_FOLDER"/../functions.sh

echo "Building resources."

cp "$root_dir/CHANGELOG.md" "$resources_dir/misc"
cp "$root_dir/PRIVACY.md" "$resources_dir/misc"

pyside6-rcc "$resources_dir/resources.qrc" -o "$app_base_dir/resources_bin.py"

dos2unix "$app_base_dir/resources_bin.py"
