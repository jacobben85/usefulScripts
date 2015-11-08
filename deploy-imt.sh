service='deportes-0.0.1-SNAPSHOT.jar'

PID=`ps -eaf | grep $service | grep -v grep | awk '{print $2}'`
if [[ "" !=  "$PID" ]]; then
  echo "killing $PID"
  kill -9 $PID
fi

mvn clean install
STATUS=$?
if [ $STATUS -eq 0 ]; then
    nohup java -jar target/$service &
fi