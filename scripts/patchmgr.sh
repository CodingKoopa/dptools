#!/bin/bash

# Prints the help message.
# Outputs:
#   - The help message.
# Returns:
#   - 0.
print_help() {
  # Keep the help string in its own variable because a single quote in a heredoc messes up syntax
  # highlighting.
  HELP_STRING="
Usage: $0 {subcommand}
Manages patches.

Subcommands:
  help
Prints this help message.
  log
Shows the Git log for the DP source code repository, for picking out commit hashes.
  exp <directory> <start commit SHA> [end commit SHA]
Exports the range of commits to the directory specified, taking into consideration any existing
patches.
"
  echo "$HELP_STRING"
  return 0
}

# Runs Git log in the current repo.
# Globals Read:
#   - common_git_args: Common Git arguments.
function log() {
  git "${common_git_args[@]}" log
}

# Exports Git commits as patches, considering existing files (e.g. if there exists patches up to
# index 0013, this function will write patches as 0014+.
# Globals Read:
#   - common_git_args: Common Git arguments.
# Arguments:
#   - Directory to write the patches to.
#   - Commit to start at.
#   - (Optional) Commit to end at. If not specified, only the starting commit will be exported.
# Outputs:
#   - Exporting status messages.
# Returns:
#   - 1 if an error occurred while exporting the patches.
#   - 2 if invalid arguments.
function exp() {
  local -r dir_arg=$1
  local -r start_c_sha=$2
  local -r end_c_sha=$3

  if [[ -z $dir_arg ]]; then
    echo "Error: output directory not given."
    return 2
  fi
  if [[ -z $start_c_sha ]]; then
    echo "Error: starting commit SHA not given."
    return 2
  fi
  if [[ -z $end_c_sha ]]; then
    local -r revision_range=(-1 "$start_c_sha")
  else
    local -r revision_range=("$start_c_sha"^.."$end_c_sha")
  fi

  local -r dir=$(realpath "$dir_arg")
  mkdir -p "$dir"

  echo "Getting current last index..."
  current_index=$(find "$dir" -name '*.patch' -printf "%f\n" | sed 's/\([0-9]\+\).*/\1/g' |
    sort -n | tail -1)
  ((current_index++))
  # Format the index as octal so that no conversion takes place.
  current_index_str=$(printf "%04o" "$current_index")

  echo "Exporting patches from commits $start_c_sha to $end_c_sha."
  if ! git "${common_git_args[@]}" format-patch -o "$dir" -N --start-number "$current_index_str" \
    "${revision_range[@]}"; then
    echo "Error: Unable to export patches."
    return 1
  fi
}

# Entrypoint for patchmgr. Runs the specified subcommand function.
# Arguments:
#   - Subcommand to run.
#   - Subcommand arguments.
# Outputs:
#   - Subcommand output.
# Returns:
#   - Subcommand return.
function patchmgr() {
  function=$1
  shift
  echo "patchmgr!"

  # For the subcommands, we would like to assume that we are in the root of the dptools directory.
  return_to_scripts=false
  if [[ ${PWD##*/} = "scripts" ]]; then
    echo "Moving out of scripts directory."
    return_to_scripts=true
    cd ..
  fi
  if [[ ! -d "scripts" ]]; then
    echo "Error: PWD not recognized as a path within dptools."
    return 1
  fi

  local -r dp_path="../dp"
  if [[ ! -d "$dp_path" ]]; then
    echo "Error: DP source code not found, tried \"$(realpath "$dp_path")\"."
    return 1
  fi
  if ! (cd "$dp_path" && git status >/dev/null); then
    echo "Error: DP directory doesn't look like a Git repo."
  fi

  local -r common_git_args=(-C "$dp_path")

  shopt -s nocasematch
  case $function in
  "log")
    log "$@"
    ;;
  "exp"*)
    exp "$@"
    ;;
  *)
    print_help
    ;;
  esac

  if [[ $return_to_scripts = true ]]; then
    cd "scripts" || echo "Unable to return to scripts directory." && return 1
  fi
}

patchmgr "$@"
