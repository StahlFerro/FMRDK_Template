#!/bin/bash

shopt -s nocasematch

if [[ $1 =~ "dev" ]]; then
  echo "Setting FLASK_ENV=development"
  export FLASK_ENV=development
elif [[ $1 =~ "prod" ]]; then
  echo "Setting FLASK_ENV=production"
  export FLASK_ENV=production
elif [[ $1 =~ "clear" || $1 =~ "clr" ]]; then
  echo "Clearing FLASK_ENV"
  unset FLASK_ENV
fi

shopt -u nocasematch
