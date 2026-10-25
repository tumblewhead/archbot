#!/usr/bin/env bash
# Reproduce exploratory finite publisher/consumer handoff evidence.
set -euo pipefail
cd "$(dirname "$0")"
build="$(mktemp -d)"
trap 'rm -rf "$build"' EXIT
cc_bin="${CC:-cc}"
common=(-std=c11 -Wall -Wextra -Werror -pedantic -Iinclude)
sources=(src/cln_numeric.c src/cln_sync_experiment.c src/cln_flow_experiment.c tests/test_flow.c)
"$cc_bin" "${common[@]}" -O2 "${sources[@]}" -o "$build/flow"
"$build/flow"
if [[ "${SANITIZE:-0}" == 1 ]]; then
  "$cc_bin" "${common[@]}" -O1 -g -fsanitize=address,undefined -fno-omit-frame-pointer \
    "${sources[@]}" -o "$build/flow_san"
  ASAN_OPTIONS=detect_leaks=1:abort_on_error=1 "$build/flow_san"
fi
