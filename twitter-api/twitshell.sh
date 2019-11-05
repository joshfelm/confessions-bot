#!/bin/bash -
#===============================================================================
#
#          FILE: twitshell.sh
#
#         USAGE: ./twitshell.sh
#
#   DESCRIPTION: 
#
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 04/11/19 19:06:23
#      REVISION:  ---
#===============================================================================

set -o nounset                                  # Treat unset variables as an error

while [ : ]
do
  python3 twitter.py
  sleep 1h
done
