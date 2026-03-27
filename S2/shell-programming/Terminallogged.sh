#!/bin/sh

if [ $# -eq 1 ]
then  
    who > user.1st
    echo "$1 user is logged at"
    grep -c $1 user.1st
else 
    echo "ple enter user name"
fi

