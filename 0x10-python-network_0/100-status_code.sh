#!/bin/bash
# post a varible
curl -sI  0.0.0.0:5000 |  awk '/HTTP\/1.0/ {print $2}'
