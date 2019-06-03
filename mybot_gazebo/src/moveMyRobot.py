#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def main():
    pub = rospy.Publisher('/mybot/leftWheel_effort_controller/command', Float64, queue_size=10)
    rospy.init_node('circler', anonymous=True)

    rate = rospy.Rate(3) # 3hz
    data = Float64()
    data = 10

    while not rospy.is_shutdown():
        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
