#!/bin/bash

set -e

CI_HOME_FOLDER=$(dirname "$(readlink -f "$0")")
readonly CI_HOME_FOLDER

source "$CI_HOME_FOLDER"/../functions.sh

pyinstaller_version="6.9.0"

mkdir -p "$build_dir"

copy_with_variables "$CI_HOME_FOLDER/version_info.py" "$build_dir"

copy_with_variables "$CI_HOME_FOLDER/windows.spec" "${build_dir}/${app_name}.spec"

init_venv "$build_dir/pyinstaller_venv"

pip install -r requirements.txt
pip install pyinstaller=="$pyinstaller_version"

pyinstaller --clean --noconfirm "${build_dir}/${app_name}.spec"
