#!/bin/bash
#
curl -s -w "%{http_code}" -o /dev/null "$1"
