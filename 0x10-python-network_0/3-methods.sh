#!/bin/bash
# accepted methos
curl -sI -X OPTIONS "$1" | grep Allow: | awk '{print $2 $3 $4}'
