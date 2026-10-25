#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
build="$(mktemp -d)"
trap 'rm -rf "$build"' EXIT
${CC:-cc} -std=c11 -O2 -Wall -Wextra -Werror -pedantic -Iinclude \
  src/cln_numeric.c src/cln_sync_experiment.c tests/test_cln.c -o "$build/cln_test"
"$build/cln_test"
