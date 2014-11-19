echo "Downloading the sample file"

rm server.log

wget http://ip-10-205-200-103.uolsite.univision.com/jbosslogs1/server.log

echo "Initiating the search"
STARTDATE=` date +"%Y-%m-%d %H:%M" -d "-2 hour"`
ENDDATE=` date +"%Y-%m-%d %k:%M"`

STARTTIME=$STARTDATE
ENDTIME=$ENDDATE

echo $STARTTIME
echo $ENDTIME

sed -n "/^$STARTTIME/ ,/^$ENDTIME/p" server.log | grep "ERROR"

# rm server.log

# wget http://linux85.qasite.univision.com/jbosslogs1/server.log

# echo "Initiating the search"
# STARTDATE=` date +"%Y-%m-%d %H:%M" -d "-3 hour"`
# ENDDATE=` date +"%Y-%m-%d %k:%M"`

# STARTTIME=$STARTDATE
# ENDTIME=$ENDDATE

# echo $STARTTIME
# echo $ENDTIME

# sed -n "/^$STARTTIME/ ,/^$ENDTIME/p" server.log | grep "ERROR"

