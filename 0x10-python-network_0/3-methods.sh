#!/bin/bash
#
curl -sI -X OPTIONS "$1" | awk '/Allow:/ {print $2 " " $3 " " $4}'
