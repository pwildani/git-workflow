#!/bin/bash
# Put symlinks to the source repo in the target directory, so that the shared
# utility libs don't have to be on the user's PATH.
#
# Usage:
#   install.sh <target-directory>
target_root="${1:-$HOME/bin}"
src_root="`dirname "$0"`"
src_root="$`cd "${src_root}" && pwd -P`"

tools="git-cleanup git-github-login git-pull-request git-start git-sync git-sync-all"

for t in $tools; do
        ln -s "${src_root}/proxy.py" "${target_root}/$t"
done
