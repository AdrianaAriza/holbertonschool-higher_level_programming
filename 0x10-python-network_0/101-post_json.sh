#!/bin/bash
# post a varible
curl -sX POST "$1" -H "Content-Type: application/json" --data-binary "@$2"
