#!/bin/sh

FILE="$1"
FILEOUT="$2"
if [ ! -f $FILE ]; then
    echo "File $FILE does not exist"
    set -e
    exit 1
fi

# Удалить \r 
awk '{gsub(/\r/,"",$0)}1' $FILE | \

# Заменить \ на \\ 
awk '{gsub(/\\/,"\\\\",$0)}1' $FILE | \

# Заменить " на \" 
awk '{gsub(/"/,"\\\"",$0)}1' | \

# Поместить строку в " \n" 
awk '{ printf "\"%s\\n\"\n", $0  }'

