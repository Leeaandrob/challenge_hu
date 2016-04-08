#!/bin/bash

export HU=hotelurbano
export HU_DB=hotelurbano_db

echo
echo "--------------------------------------------"
echo "This script will install PostgreSQL."
echo "and create alfresco database and user."
echo "You may be prompted for sudo password."
echo "--------------------------------------------"
echo

read -e -p "Install PostgreSQL database? [y/n] " -i "n" installpg
if [ "$installpg" = "y" ]; then
  sudo apt-get install postgresql
  echo
  echo "You will now set the default password for the postgres user."
  echo "This will open a psql terminal, enter:"
  echo
  echo "\\password postgres"
  echo
  echo "and follow instructions for setting postgres admin password."
  echo "Press Ctrl+D or type \\q to quit psql terminal"
  echo "START psql --------"
  sudo -u postgres psql postgres
  echo "END psql --------"
  echo
fi

read -e -p "Create HU_DB Database and user? [y/n] " -i "n" createdb
if [ "$createdb" = "y" ]; then
  sudo -u postgres createuser -D -A -P $HU
  sudo -u postgres createdb -O $HU $HUDB
  echo
fi
