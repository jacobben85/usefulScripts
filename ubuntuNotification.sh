#!/bin/bash

# notify-send "Notification" "Testing messages" -i $(pwd)/logo.png -t 5000
# paplay $(pwd)/beep.ogg

#
# #!/bin/sh
# touch $HOME/.dbus/Xdbus
# chmod 600 $HOME/.dbus/Xdbus
# env | grep DBUS_SESSION_BUS_ADDRESS > $HOME/.dbus/Xdbus
# echo 'export DBUS_SESSION_BUS_ADDRESS' >> $HOME/.dbus/Xdbus
# exit 0
#

if [ -r ~/.dbus/Xdbus ]; then
  . ~/.dbus/Xdbus
fi

notify-send "Time Check" "$(date)" -i ~/usefulScripts/logo.png -t 5000
# paplay ~/usefulScripts/beep.ogg
