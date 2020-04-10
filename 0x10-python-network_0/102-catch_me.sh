#!/bin/bash
# post a varible
curl -d user_id=98 -sL -X PUT -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
