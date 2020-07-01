#!/usr/bin/env python


#Este programa é testado no Gazebo Simulator
#Este script usa o pacote cv_bridge para converter imagens vindas do tópico
#sensor_msgs/Image para mensagens OpenCV para serem analizadas pelo pacote
#pyzbar, a procura de QR Codes. Um código bem simples, em que o robô p3dx
#irá girar em torno do eixo Z até encontrar uma parede que tenha um QR Code.
#Os valores das coordenadas de posição do robô são captadas usando odometria

import rospy, cv2, cv_bridge, numpy, math, argparse
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

from pyzbar import pyzbar



class Follower:

        def __init__(self):

                self.bridge = cv_bridge.CvBridge()
                cv2.namedWindow("window", 1)

                self.image_sub = rospy.Subscriber('/p3dx/front_camera/image_raw',
                        Image, self.image_callback)

                self.cmd_vel_pub = rospy.Publisher('p3dx/cmd_vel',
                        Twist, queue_size=1)

                self.odom_sub = rospy.Subscriber('p3dx/odom',Odometry,self.callback_odom)  

                self.twist = Twist()
                self.qr = 0

        def callback_odom(self,msg): 
                xr=msg.pose.pose.position.x
                yr=msg.pose.pose.positio

        def image_callback(self, msg):

                image = self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
                

                if self.qr==0:
                        self.twist.angular.z = -math.pi/10
                        self.cmd_vel_pub.publish(self.twist)

                else:
                        self.twist.angular.z = 0
                        self.cmd_vel_pub.publish(self.twist)

                cv2.imshow("window", image)
                cv2.imwrite("qrcode.png", image)
                img_qr = cv2.imread("qrcode.png") 

                barcodes = pyzbar.decode(img_qr)

                for barcode in barcodes:
                	(x, y, w, h) = barcode.rect
                	cv2.rectangle(img_qr, (x, y), (x + w, y + h), (0, 0, 255), 2)

                	barcodeData = barcode.data.decode("utf-8")
                	barcodeType = barcode.type


                	text = "{} ({})".format(barcodeData, barcodeType)
                	print(text)
                        self.qr=1
                        cv2.putText(img_qr, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
		0.5, (0, 0, 255), 2)
                cv2.imshow("Imagem", img_qr)
                cv2.waitKey(3)
		##

rospy.init_node('qr_code')
follower = Follower()
rospy.spin()

