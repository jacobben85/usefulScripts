if [ -r ~/.dbus/Xdbus ]; then
  . ~/.dbus/Xdbus
fi

CURRENTDATE=` date +"%Y-%m-%d" -d "-1 hour"`
CURRENTDATE=$CURRENTDATE

CURRENTHOUR=` date +"%m-%d-%Y @ %H" -d "-1 hour"`
CURRENTHOUR=$CURRENTHOUR

echo "Looking up errors in Ooyala logs for :"
echo $CURRENTHOUR

wget -q http://u1819.uolsite.univision.com/applogs/mylog_$CURRENTDATE

echo ""
echo "Total number of error reports in logs :"
grep -c 'Error' mylog_$CURRENTDATE

ERRORCOUNT=`grep -c "$CURRENTHOUR:.*:.* Error" mylog_$CURRENTDATE`

notify-send "Ooyala log checker" "Last hour errors : $ERRORCOUNT" -i ~/usefulScripts/logo.png -t 5000

if [ $ERRORCOUNT = "0" ]; then
	echo ""
	echo "No Errors in last hour"
else
	echo ""
	echo "Number of errors in last hour :"
	echo $ERRORCOUNT

	echo ""
	echo "Errors in last hour :"
	grep -C 3 'Error' mylog_$CURRENTDATE | grep "$CURRENTHOUR:.*:.*Start send request GET: /v2/assets/.* to Ooyala api" | grep -o '[0-9]\{5,7\}'

	echo ""
	echo "Details from Log :"
	grep -C 3 "$CURRENTHOUR:.*:.* Error" mylog_$CURRENTDATE
	echo ""
fi

rm mylog_$CURRENTDATE
