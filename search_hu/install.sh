#! /bin/bash

if [ `uname` == "Linux"  ]; then
	`sh postgres.sh`
	echo "It worked"
else
	if [ `which brew` == "/usr/local/bin/brew" ]; then
		sh postgres_osx.sh
	else
		/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	fi
fi
