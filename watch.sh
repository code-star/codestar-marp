#!/bin/bash

marp -s --theme theme/codestar.css . &

fswatch -o theme/*.scss | while read f
do
  echo "Rebuilding 'theme/codestar.css'"
  ./build.sh
done
