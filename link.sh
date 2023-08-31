#!/usr/bin/env bash

# For easy testing the plugin in Anki.
# Just run this script once then open Anki.

plugin_name=LibreMemChess
plugin_path_linux=~/.local/share/Anki2/addons21
plugin_path_mac=~/Library/Application\ Support/Anki2/addons21

if [ -d "$plugin_path_linux" ]; then
    ln -s -f $(pwd)/src $plugin_path_linux/$plugin_name
    exit 0
fi

if [ -d "$plugin_path_mac" ]; then
    ln -s -f $(pwd)/src $plugin_path_mac/$plugin_name
fi
