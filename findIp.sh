ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1  -d'/'

ifconfig | perl -nle 's/dr:(\S+)/print $1/e'

ifconfig | awk '/inet addr/{print substr($2,6)}'
