#!/bin/bash

# Dump the C array lines here.
text=""

while IFS= read -r line; do
  if [[ -n $line ]]; then
    ./textconv.py decode "$line"
  fi
done <<<"$text"
