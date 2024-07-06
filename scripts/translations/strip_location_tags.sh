#!/bin/bash

set -e

CI_HOME_FOLDER=$(dirname "$(readlink -f "$0")")
readonly CI_HOME_FOLDER

source "$CI_HOME_FOLDER"/../functions.sh

for ts_file in "$resources_dir"/translations/*.ts; do
    if [[ $(basename "$ts_file") == "en_US.ts" ]]; then
        continue
    fi

    sed -i -E '/^[[:space:]]*<location .*\/>$/d' "$ts_file"
done
