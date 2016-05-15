#!/bin/sh
pip freeze |grep -v wheel | awk -F"==" ' { print $1 } ' > requirements.txt
