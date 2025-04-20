#/data/data/com.termux/files/usr/bin/bash



pythonId=$(pgrep python3)


if [ -n "${pythonId}" ]; then
    echo "killing running py process.."
    kill -9 "$pythonId"
    killed=true

else
    echo "no py process running."
    echo "starting server"

    python3 hi.py
    
fi


echo "$pythonid"

