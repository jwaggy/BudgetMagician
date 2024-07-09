root_dir=$(realpath "$(pwd)")
readonly root_dir

readonly resources_dir="$root_dir/resources"
readonly scripts_dir="$root_dir/scripts"
readonly build_dir="$root_dir/build"
readonly dist_dir="$root_dir/dist"
readonly app_module="BudgetMagician"
app_base_dir=$(realpath "./$app_module")
readonly app_base_dir
readonly app_repo_slug="jwaggy/BudgetMagician"
app_display_name=$(sed -n 's/__display_name__ = "\([^"]*\).*/\1/p' "$app_base_dir/version.py")
readonly app_display_name
app_name=$(sed -n 's/__app_name__ = "\([^"]*\).*/\1/p' "$app_base_dir/version.py")
readonly app_name
app_id=$(sed -n 's/__app_id__ = "\([^"]*\).*/\1/p' "$app_base_dir/version.py")
readonly app_id
app_version=$(sed -n 's/__version__ = "\([^"]*\).*/\1/p' "$app_base_dir/version.py")
readonly app_version
app_version_date=$(sed -n 's/__version_date__ = "\([^"]*\).*/\1/p' "$app_base_dir/version.py")
readonly app_version_date
app_author=$(sed -n 's/__author_name__ = "\([^"]*\).*/\1/p' "$app_base_dir/version.py")
readonly app_author
app_author_contact=$(sed -n 's/__author_contact__ = "\([^"]*\).*/\1/p' "$app_base_dir/version.py")
readonly app_author_contact
app_url=$(sed -n 's/__app_url__ = "\([^"]*\).*/\1/p' "$app_base_dir/version.py")
readonly app_url
app_bugtracker_url=$(sed -n 's/__app_bugtracker_url__ = "\([^"]*\).*/\1/p' "$app_base_dir/version.py")
readonly app_bugtracker_url

export resources_dir scripts_dir build_dir dist_dir app_module app_base_dir app_repo_slug app_display_name app_name app_id app_version app_version_date app_author app_author_contact app_url app_bugtracker_url

die()
{
    printf '%s\n' "$*" >&2
    exit 1
}

activate_venv()
{
    local venv_dir="$1"

    if [[ -f "$venv_dir/Scripts/activate" ]]; then
        source "$venv_dir/Scripts/activate"
    else
        source "$venv_dir/bin/activate"
    fi
}

init_venv()
{
    local venv_dir="$1"

    if [[ ! -d "$venv_dir" ]]; then
        python -m venv "$venv_dir"

        activate_venv "$venv_dir"

        python -m pip install --upgrade pip

    else
        activate_venv "$venv_dir"
    fi
}

replace_variables()
{
    local target_file="$1"

    [[ ! -f "$target_file" ]] && return

    vars=$(env | cut -d '=' -f1 | grep "^app_")

    while IFS= read -r var; do
        eval replace='$'$var

        [[ -z "$replace" ]] && die "$var variable is empty."

        sed -i "s#{$var}#$replace#g" "$target_file"
    done <<< "$vars"
}

copy_with_variables()
{
    local source="$1"
    local destination=$2

    if [[ -d "$destination" ]]; then
        dest_file=$(realpath "$destination")/$(basename "$source")
    else
        dest_file="$destination"
    fi

    cp "$source" "$dest_file"

    replace_variables "$dest_file"
}
