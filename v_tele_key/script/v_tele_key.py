import rospy
from geometry_msgs.msg import Twist

msg = """

Control 
---------------------------
Moving around:
   q    w    e
   a    s    d
        x
q/e : increase/decrease velocity 
w/x : forward/backward
a/d : left/right
space key, s : force stop
Anykey to quit

"""



# -------------- Function Teleop -------------------------
def tele_key():
    #---------  สร้าง node ชื่อ v_tele_node เพื่อใช้สื้อสารกับ Ros Master
    rospy.init_node('v_teleop_node')
    #--------- กำหนดรูปแบบของค่าที่จะส่งออกไปของ node ( ใช้ Class Twist )  โดยเลือก Topic เป็น cmd_vel เพื่อที่จะสือสารกับ plug in  differential drive
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    twist = Twist()
    velocity = 0.0

    while(1):
        key = input("Command : ")
        if key == 'w':
            twist.linear.x = velocity
            print("move forward :\tlinear vel %f\t angular vel %f " % (twist.linear.x, twist.angular.z))

        elif key == 'q' and velocity >= 0.01:
            velocity -= 0.2
            print("decrease velocity :\tvelocity %f" % (velocity))

        elif key == 'e':
            velocity += 0.2
            print("increase velocity :\tvelocity %f" % (velocity))

        elif key == 'x':
            twist.linear.x = -velocity
            print("move backward :\tlinear vel %f\t angular vel %f " % (twist.linear.x, twist.angular.z))

        elif key == 'a':
            twist.angular.z = velocity
            print("turn left :\tlinear vel %f\t angular vel %f " % (twist.linear.x, twist.angular.z))

        elif key == 'd':
            twist.angular.z = -velocity
            print("turn right :\tlinear vel %f\t angular vel %f " % (twist.linear.x, twist.angular.z))

        elif key == ' ' or key == 's':
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            print("STOP :\tlinear vel %f\t angular vel %f " % (twist.linear.x, twist.angular.z))

        else:
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            pub.publish(twist)
            print(" Quit ")
            break
        # Publish ออกไปยัง topic cmd_vel
        
        pub.publish(twist)
        rate.sleep()


if __name__=="__main__":
    try:
        print(msg)
        tele_key()
    except rospy.ROSInterruptException:
        pass


