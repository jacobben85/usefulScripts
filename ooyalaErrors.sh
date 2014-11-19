CURRENTDATE=` date +"%Y-%m-%d" -d "-1 day"`
CURRENTDATE=$CURRENTDATE

STRINGMATCH= 'Error'

echo "Looking up errors in Ooyala logs for :"
echo $CURRENTDATE
echo "\n\n"

wget http://u1819.uolsite.univision.com/applogs/mylog_$CURRENTDATE

grep -C 3 'Error' mylog_$CURRENTDATE

echo "\n\nFailed ingestions for :"
grep -C 3 'Error' mylog_$CURRENTDATE | grep "Start send request GET: /v2/assets/.* to Ooyala api" | grep -o '[0-9]\{5,7\}'

echo "\n\nNumber of error reports in logs :"
grep -c 'Error' mylog_$CURRENTDATE

rm mylog_$CURRENTDATE
