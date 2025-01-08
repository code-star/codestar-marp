#!/bin/bash

marp -s --theme theme/codestar.css . &

fswatch -o theme/*.scss | while read f
do
  echo "Reuilding 'theme/codestar.css'"
  ./build.sh
done
