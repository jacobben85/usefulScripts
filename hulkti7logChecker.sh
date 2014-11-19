echo "Downloading the sample file"

rm server.log

wget http://applogs.qasite.univision.com/nj3-qasite/jboss/Hulk-ti7-eap6/standalone1/server.log 

echo "Initiating the search"
STARTDATE=` date +"%Y-%m-%d %H:%M" -d "-5 mins"`
ENDDATE=` date +"%Y-%m-%d %k:%M"`

STARTTIME=$STARTDATE
ENDTIME=$ENDDATE

echo $STARTTIME
echo $ENDTIME

sed -n "/^$STARTTIME/ ,$ p" server.log | grep "ERROR"

#tail server.log

rm server.log.1

wget http://applogs.qasite.univision.com/nj3-qasite/jboss/Hulk-ti7-eap6/standalone2/server.log

echo "Initiating the search"
STARTDATE=` date +"%Y-%m-%d %H:%M" -d "-5 mins"`
ENDDATE=` date +"%Y-%m-%d %k:%M"`

STARTTIME=$STARTDATE
ENDTIME=$ENDDATE

echo $STARTTIME
echo $ENDTIME

sed -n "/^$STARTTIME/ ,$ p" server.log.1 | grep "ERROR"

#tail server.log
