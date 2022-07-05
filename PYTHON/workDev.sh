#! /usr/bin/bash

clear
echo -n "DESIGN LINES:"
wlod
echo "MOST RECENT UPDATE:"
ls -lrt `find ${DEV_DSN_DIR} -type f` | tail -1 | awk '{print $6 " " $7 " " $8 " " $9}'
sleep 1
more `find ${DEV_DSN_DIR} -type f | egrep -vi 'swp|nohup' | sort -R`
vi -R `find ${DEV_DSN_DIR} -type f | egrep -vi 'swp|nohup' | sort -R`

clear
echo -n "SOURCE LINES:"
wloc
echo "MOST RECENT UPDATES:"
rm /tmp/srcList 2>/dev/null
ls -lrt `find ${DEV_JAVA_SRC_DIR} -type f -name "*.java"` | tail -1 | awk '{print $9}' >> /tmp/srcList
ls -lrt `find ${DEV_NODE_SRC_DIR} -type f -name "*.js"` | tail -1 | awk '{print $9}' >> /tmp/srcList
ls -lrt `find ${DEV_RUBY_SRC_DIR} -type f -name "*.rb"` | tail -1 | awk '{print $9}' >> /tmp/srcList

ls -lrt `cat /tmp/srcList` | awk '{print $6 " " $7 " " $8 " " $9}'

# More all source
clear; more `find ${DEV_JAVA_SRC_DIR} -type f -name "*.java" | egrep -vi 'swp|nohup' | sort -R`
clear; more `find ${DEV_NODE_SRC_DIR} -type f -name "*.js" | egrep -vi 'swp|nohup' | sort -R`
clear; more `find ${DEV_RUBY_SRC_DIR} -type f -name "*.rb" | egrep -vi 'swp|nohup' | sort -R`

function idea() { nohup /opt/idea-IC-182.3684.101/bin/idea.sh  >> $HOME/.LOGS/NOHUP/intellijIdea & }
export -f idea

function pyc() { nohup /bin/sh /snap/pycharm-community/current/bin/pycharm.sh >> $HOME/.LOGS/NOHUP/intellijPyCharm & }
export -f pyc

function brac() { nohup brackets >> $HOME/.LOGS/NOHUP/brackets & }
export -f brac

idea
pyc
brac
