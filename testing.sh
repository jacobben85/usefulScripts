# if [ "$TERM" = xterm ] || [ "$TERM" = dtterm ]; then
#    alias cd=Xcd
#    Xcd ()
#    {
#       if [ $# -ne 0 ]; then
#          'cd' "$@"
#       else
#          'cd'
#       fi
#       NAME="$(uname -n):${PWD}"
#       # reset name of xterm title bar & icon to $NAME
#       echo "\033]0;${NAME}\007\c"  # set title bar & icon
#    }
#    Xcd .
# elif [ "$TERM" = hpterm ]; then
#    alias cd=Hcd
#    Hcd ()
#    {
#       if [ $# -ne 0 ]; then
#          'cd' "$@"
#       else
#          'cd'
#       fi
#       NAME="$(uname -n):${PWD}"
#       LEN=`echo "$NAME\c" | wc -c`
#       # reset name of hpterm title bar & icon to $NAME
#       echo "\033&f0k${LEN}D${NAME}\c"   # set title bar
#       echo "\033&f-1k${LEN}D${NAME}\c"  # set icon
#    }
#    Hcd .
# fi

echo "Greet user"
tt=`date +"%T" | cut -c1-2`
NAME=`grep "^$LOGNAME" /etc/passwd | awk -F: ' {print $5}'`
echo "\n\n\n"
tput smso
if [ $tt -gt 0 -a $tt -lt 12 ]
then
   echo " $NAME !!!!!!    GOOD MORNING !!!!!!"
elif [ $tt -gt 12 -a $tt -le 16 ]
then
   echo " $NAME !!!!!!  GOOD AFTERNOON !!!!!!"
else
   echo " $NAME !!!!!!   GOOD EVENING !!!!!!"
fi
tput rmso

echo "Show directory in the prompt"
export PS1='$PWD $'

