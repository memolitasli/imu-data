#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import Imu
import datetime
import pyrebase

firebaseConfig = {
'firebase':'config bilgileri'
}
firebase = pyrebase.initialize_app(firebaseConfig)

class subClass():
    def __init__(self):
        self.logoCiz()
        rospy.init_node("imuDataSub")
        rospy.Subscriber("/mavros/imu/data",Imu,self.imuCallBack)
        rospy.spin()
    def logoCiz(self):
            print('''
            - + - + @ @ @ - + - + - + -  + -
            - + - + - + -@ - + - + - + - + + 
            - + - + - + - @ - + - + - + -  +
            - + - + - + @  @ - + - + - + - +
            - + - + -  @ -  @ - - @ @  - + -
            - + - + - @      @ - @ - + - + -
            - - -@ @ @       @ @ - + - + - +
            - + - + - + Memoli - + - + - + -
            ''')
    def imuCallBack(self,mesaj):
        txtFile = open("imuVerileri.txt","a+")
        txtFile.write("---------------------------------------"+"\n")
        txtFile.write(str(datetime.datetime.now()))
        txtFile.write("Angular Velocity Verileri : ")
        txtFile.write("X : "+str(mesaj.angular_velocity.x)+"\n")
        txtFile.write("Y : "+str(mesaj.angular_velocity.y)+"\n")
        txtFile.write("Z : "+str(mesaj.angular_velocity.z)+"\n")
        txtFile.write("Linear Acceleration Verileri : "+"\n")
        txtFile.write("X : "+str(mesaj.linear_acceleration.x)+"\n")
        txtFile.write("Y : "+str(mesaj.linear_acceleration.y)+"\n")
        txtFile.write("Z : "+str(mesaj.linear_acceleration.z)+"\n \n")
        txtFile.write("Oryantasyon Verileri  :"+"\n")
        txtFile.write("X : "+str(mesaj.orientation.x)+"\n")
        txtFile.write("Y : "+str(mesaj.orientation.y)+"\n")
        txtFile.write("Z : "+str(mesaj.orientation.z)+"\n")
        txtFile.write("W : "+str(mesaj.orientation.w)+"\n")
        txtFile.write("---------------------------------------"+"\n")

    def firebaseVeriYukle(self,mesaj):
        db = firebase.database()
        data = {
            "angular_velocity":{
                "x":str(mesaj.angular_velocity.x),
                "y":str(mesaj.angular_velocity.y),
                "z":str(mesaj.angular_velocity.z)
            },
            "linear_acceleration":{
                "x":str(mesaj.linear_acceleration.x),
                "y":str(mesaj.linear_acceleration.y),
                "z":str(mesaj.linear_acceleration.z)
            },
            "oriantation":{
                "x":str(mesaj.orientation.x),
                "y":str(mesaj.orientation.y),
                "z":str(mesaj.orientation.z),
                "w":str(mesaj.orientation.w)
            }
        }
        db.child(str(datetime.datetime.now())).set(data)

nesne = subClass()