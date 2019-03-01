#!/bin/bash
basedir=$(pwd)

ls /opt/stalone_tray_clock

if [ $? -ne 0 ] ; then
    sudo mkdir /opt/stalone_tray_clock
fi

sudo cp stalone_tray_clock.py /opt/stalone_tray_clock/

cat $HOME/.config/openbox/autostart > ~/Downloads/temp.tmp
temp=$(sed -n '/stalone_tray_clock &/p' ~/Downloads/temp.tmp)
if [ ${#temp} -gt 0 ] ; then
    echo "--------------------------------------"
    echo "stalone_tray_clock já estava configurado."
    echo "--------------------------------------"
    rm ~/Downloads/temp.tmp
else
    echo "stalone_tray_clock &" >> ~/Downloads/temp.tmp
    cp ~/Downloads/temp.tmp $HOME/.config/openbox/autostart
    rm ~/Downloads/temp.tmp
    echo "--------------------------------------"
    echo "stalone_tray_clock foi configurado."
    echo "--------------------------------------"
fi

ls /usr/bin/stalone_tray_clock

if [ $? -ne 0 ] ; then
    cd /usr/bin/
    sudo ln -s /opt/stalone_tray_clock/stalone_tray_clock.py stalone_tray_clock
fi
