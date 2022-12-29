#SPDX-FileCopyrightText:2022 Tarou Sato<s21c1023nb@s.chibakoudai.jp>
##SPDX-License-Identifier:BSD-3-Clause#SPDX-FileCopyrightText:2022 Tarou Sato<s21c1023nb@s.chibakoudai.jp>
#SPDX-License-Identifier:BSD-3-Clause

import rclpy
import sys
import random
from rclpy.node import Node
from person_msgs.msg import Person #使う型を変更

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Person, "person", 10) #変更
n = 0
sam=0
def cb():

    global n,sam
    msg = Person()         #受信するデータの型を変更
    n = random.randint(0, 7)
    
    if sam==1:
        sys.exit()

    if n==0:
        msg.name = "ハンバーガー"  #msgファイルに書いた「name」
        msg.price = 100            #msgファイルに書いた「age」
            
    elif n==1:
        msg.name = "チーズバーガー"  #msgファイルに書いた「name」
        msg.price = 130            #msgファイルに書いた「age」
    elif n==2:
        msg.name = "Mocバーガー"  #msgファイルに書いた「name
        msg.price = 98      
    elif n==3:
        msg.name = "タコライスバーガー"  #msgファイルに書いた「name」
        msg.price = 200
    elif n==4:
        msg.name = "タコ焼きバーガー"  #msgファイルに書いた「nam
        msg.price = 200                                                                                                                                                                 
    elif n==5:   
        msg.name = "バーガー味シェイク"  #msgファイルに書いた「name」
        msg.price = 30
    elif n==6:
        msg.name = "Mocのポテトs"  #msgファイルに書いた「name」
        msg.price = 150
           
    else:
        msg.name = "ありがとうございました。"  #msgファイルに書いた「nfme」
        sam=1
    pub.publish(msg)

node.create_timer(0.5, cb)
rclpy.spin(node)

