#!/usr/bin/bash

echo "
============ SlapTap Userbot ============

Starting Now...

Copyright (c) 2021 InfinityGo | @SlapTap
"

start_nexaub () {
    if [[ -z "$PYRO_STR_SESSION" ]]
    then
	    echo "Please add Pyrogram String Session"
    else
	    python3 -m nexa_userbot
    fi
  }

_install_nexaub () {
    start_nexaub
  }

_install_nexaub
