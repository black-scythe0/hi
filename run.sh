#/data/data/com.termux/files/usr/bin/bash

yel="\e[1;33m"
whi="\e[0m"

pythonId=$(pgrep python3)


if [ -n "${pythonId}" ]; then
    echo "killing running py process.."
    kill -9 "$pythonId"
    killed=true

else
    echo "no py process running."
    echo "starting server"
    date>> log.txt
    echo " ">> log.txt
    
    python3 hi.py --verbose 2>> log.txt
    echo " ">> log.txt
    echo " ">> log.txt
fi

sleep 3 &&

if [ -n "${pythonId}" ];then
    echo "server is running.."

else
    echo "server not running"
    echo -e "${yel}--see log.txt fro more info--${whi}"


fi


echo "$pythonid"

