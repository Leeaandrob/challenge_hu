#!/bin/bash

brew update
brew doctor
brew install postgresql
initdb /usr/local/var/postgres -E utf8
pg_ctl -V | grep "[0-9]" | sed -e "s/[a-zA-Z].//g" | sed -e "s/_()//g"
gem install lunchy
