#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch moc talk_listen.launch.py > /tmp/moc.log

cat /tmp/moc.log |
 grep 'Listen: person_msgs.msg.Person(name='チーズバーガー', price=130)'
