#! /bin/bash
if [ -z "$1" ]
then
  robot -P ./Libs -d Results Tests
else
  robot -P ./Libs -d Results -i $1 Tests
fi