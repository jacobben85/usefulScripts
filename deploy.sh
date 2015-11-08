service=mysql

# If mysql server is not running start the service
if (( $(ps -ef | grep -v grep | grep $service | wc -l) > 0 ))
then
echo "$service is already running"
else
echo "Starting Mysql"
$service.server start
fi

# Build project
mvn -f /Users/jbjohn/Documents/misc/univision-push-alerts/pom.xml clean install

STATUS=$?
if [ $STATUS -eq 0 ]; then
#If tomcat is already running stop the service
if (( $(ps -ef | grep -v grep | grep tomcat | wc -l) > 0 ))
then
echo "Stopping tomcat"
sh bin/catalina.sh stop
fi

sleep 1

# Remove the Root director and copy the new build
echo "Deploying ROOT.war"
rm -Rf webapps/ROOT*
cp /Users/jbjohn/Documents/misc/univision-push-alerts/target/univision-push-alerts-1.0-SNAPSHOT.war /Users/jbjohn/misc/apache-tomcat-8.0.27/webapps/ROOT.war
sleep 1

# Start tomcat again
echo "Starting tomcat"
sh bin/catalina.sh start
else
echo "Mavel build failed"
fi