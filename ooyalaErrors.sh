CURRENTDATE=` date +"%Y-%m-%d" -d "-1 hour"`
CURRENTDATE=$CURRENTDATE

CURRENTHOUR=` date +"%m-%d-%Y @ %H" -d "-1 hour"`
CURRENTHOUR=$CURRENTHOUR

echo "Looking up errors in Ooyala logs for :"
echo $CURRENTDATE

echo "Hour :"
echo $CURRENTHOUR

wget http://u1819.uolsite.univision.com/applogs/mylog_$CURRENTDATE

echo ""
echo "Number of error reports in logs :"
grep -c 'Error' mylog_$CURRENTDATE

echo ""
echo "Errors in last hour :"
grep -C 3 'Error' mylog_$CURRENTDATE | grep "$CURRENTHOUR:.*:.*Start send request GET: /v2/assets/.* to Ooyala api" | grep -o '[0-9]\{5,7\}'

echo ""
echo "Details from Log :"
grep -C 3 "$CURRENTHOUR:.*:.* Error" mylog_$CURRENTDATE

rm mylog_$CURRENTDATE
