#!/bin/bash

set -e

CI_HOME_FOLDER=$(dirname "$(readlink -f "$0")")
readonly CI_HOME_FOLDER

source "$CI_HOME_FOLDER"/../functions.sh

echo "Building .ui files."

files="$resources_dir/ui/*"

for ui_source_file in $files; do
    ui_source=$(basename "$ui_source_file")
    ui_destination="${ui_source%.*}Ui.py"

    echo "Converting $ui_source to $ui_destination"


    if [[ "$ui_source" == "MainWindow.ui" ]]; then
        pyside6-uic "$ui_source_file" -o "$app_base_dir/magician/$ui_destination"
    else
        pyside6-uic "$ui_source_file" -o "$app_base_dir/dialogs/$ui_destination"
    fi
done

sed -i 's/^#.*$//g' "$app_base_dir/dialogs"/*Ui.py

dos2unix "$app_base_dir/dialogs"/*Ui.py
dos2unix "$app_base_dir/magician"/*Ui.py

black --line-length 180 "$app_base_dir/dialogs"/*Ui.py
black --line-length 180 "$app_base_dir/magician"/*Ui.py
