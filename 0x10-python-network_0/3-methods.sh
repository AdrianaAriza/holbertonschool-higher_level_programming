#!/bin/bash
# accepted methos
curl -sI -X OPTIONS "$1" | awk '/Allow/ {print $2 $3 $4}' 
