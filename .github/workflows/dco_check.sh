#!/usr/bin/env bash
set -eo pipefail
revs=$(git rev-list "HEAD") || exit 1
failed=0
for commit in $revs; do
    if git show -s --format=%B "${commit}" | grep >/dev/null 2>&1 "Signed-off-by: "; then
        echo -e "\u2714 $(git show -s --format='%h %s' $commit)"
    else
        echo -e "\u2718 $(git show -s --format='%h %s' $commit)"
        failed=1
    fi
done
[ $failed -eq 0 ] || exit 1
