if [ -z "$var" ]
then
  robot -P ./Libs -d Results Tests
else
  robot -P ./Libs -d Results -i $1 Tests
fi