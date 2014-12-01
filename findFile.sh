if [ $# -ne 2 ]
then
   echo "Usage : $0 <search pattern for files> <string to be searched>"
   echo
   exit
fi

PWD=`pwd`
for file in `find $PWD -name "$1"`
do
  grep -l "$2" $file
done
