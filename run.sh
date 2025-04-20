#/data/data/com.termux/files/usr/bin/bash



pythonId=$(pgrep python3)


if [ -n "${pythonId}" ]; then
    echo "killing running py process.."
    kill -9 "$pythonId"
    killed=true

else
    echo "no py process running."
    echo "starting server"
    echo " see error.txt for more info "
    date>> error.txt
    echo " ">> error.txt
    
    python3 hi.py --verbose 2>> error.txt
    echo " ">> error.txt
    echo " ">> error.txt
fi


echo "$pythonid"

