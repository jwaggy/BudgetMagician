#!/bin/bash

set -e

CI_HOME_FOLDER=$(dirname "$(readlink -f "$0")")
readonly CI_HOME_FOLDER

source "$CI_HOME_FOLDER"/../functions.sh

iscc="/c/Program Files (x86)/Inno Setup 6/ISCC.exe"

echo "Building installer"

cd "$dist_dir/$app_name"

app_source=$(pwd -W)

copy_with_variables "$CI_HOME_FOLDER/installer_template.iss" "$build_dir/installer.iss"

sed -i "s#{app_source}#$app_source#g" "$build_dir/installer.iss"

cd "$app_base_dir"

"$iscc" //O"dist" //F"$app_name-$app_version-win64-install" "$build_dir/installer.iss"

echo "Building portable zip"

cd "$dist_dir"

mkdir "$app_name/portable_data"

PATH="/c/Program Files/7-Zip:$PATH"

7z a -tzip -r "$app_name-$app_version-win64-portable.zip" "$app_name"

rmdir "$app_name/portable_data"
