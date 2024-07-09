#!/bin/bash

set -e

CI_HOME_FOLDER=$(dirname "$(readlink -f "$0")")
readonly CI_HOME_FOLDER

source "$CI_HOME_FOLDER"/../functions.sh

list_proofed()
{
    crowdin.bat status proofreading --no-progress --no-colors -c "$CI_HOME_FOLDER/crowdin.yml" --identity "/d/crowdin/crowdin.yml" --base-path "." | grep "%" | grep -v " 0%" | sed -E "s/[[:space:]]*- (.+): [[:digit:]]+%/\1/"
}

if [[ "$1" == "list" ]]; then
    list_proofed
    exit 0
fi

if [[ -n "$1" ]]; then
    echo "Selected languages: $@"
    IFS=' ' read -a languages <<< "$@"
else
    languages=$(list_proofed | cut -d' ' -f1)
fi

for current_language in ${languages[@]}; do
    echo "Downloading language $current_language"
    crowdin.bat download -c "$CI_HOME_FOLDER/crowdin.yml" --identity "/d/crowdin/crowdin.yml" --base-path "." --skip-untranslated-strings --export-only-approved --language="$current_language"
done

"$CI_HOME_FOLDER/strip_locations.sh"
