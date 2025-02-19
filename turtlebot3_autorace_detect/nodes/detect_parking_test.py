import rospy
import os
from enum import Enum
from std_msgs.msg import UInt8, Float64
from sensor_msgs.msg import LaserScan
from turtlebot3_autorace_msgs.msg import MovingParam


class DetectParking():
    def __init__(self):
        # subscribes state
        # self.sub_scan_obstacle = rospy.Subscriber('/detect/scan', LaserScan, self.cbScanObstacle, queue_size=1)
        self.sub_parking_order = rospy.Subscriber('/detect/parking_order', UInt8, self.customParking(), queue_size=1)
        self.sub_moving_completed = rospy.Subscriber('/control/moving/complete', UInt8, self.cbMovingComplete,
                                                     queue_size=1)

        # publishes state
        self.pub_parking_return = rospy.Publisher('/detect/parking_stamped', UInt8, queue_size=1)
        self.pub_moving = rospy.Publisher('/control/moving/state', MovingParam, queue_size=1)
        self.pub_max_vel = rospy.Publisher('/control/max_vel', Float64, queue_size=1)

        self.StepOfParking = Enum('StepOfParking', 'parking exit')
        self.start_obstacle_detection = False
        self.is_obstacle_detected_R = False
        self.is_obstacle_detected_L = False
        self.is_moving_complete = False

    def cbMovingComplete(self, data):
        self.is_moving_complete = True

    def customParking(self, order):
        msg_pub_parking_return = UInt8()

        rospy.loginfo("Now motion")
        msg_pub_max_vel = Float64()
        msg_pub_max_vel.data = 0.00
        self.pub_max_vel.publish(msg_pub_max_vel)

        rospy.sleep(1)

        rospy.loginfo("go straight")
        msg_moving = MovingParam()
        msg_moving.moving_type = 4
        msg_moving.moving_value_angular = 0.0
        msg_moving.moving_value_linear = 0.45
        self.pub_moving.publish(msg_moving)
        while True:
            if self.is_moving_complete == True:
                break
        self.is_moving_complete = False

        rospy.sleep(1)

        rospy.loginfo("go left")
        msg_moving = MovingParam()
        msg_moving.moving_type = 2
        msg_moving.moving_value_angular = 90
        msg_moving.moving_value_linear = 0.0
        self.pub_moving.publish(msg_moving)
        while True:
            if self.is_moving_complete == True:
                break
        self.is_moving_complete = False

        rospy.sleep(1)

        rospy.loginfo("go straight")
        msg_moving = MovingParam()
        msg_moving.moving_type = 4
        msg_moving.moving_value_angular = 0.0
        msg_moving.moving_value_linear = 1.0
        self.pub_moving.publish(msg_moving)
        while True:
            if self.is_moving_complete == True:
                break
        self.is_moving_complete = False

        rospy.sleep(1)

        rospy.loginfo("right parking is clear")
        rospy.loginfo("go right")
        msg_moving = MovingParam()
        msg_moving.moving_type = 3
        msg_moving.moving_value_angular = 90
        msg_moving.moving_value_linear = 0.0
        self.pub_moving.publish(msg_moving)
        while True:
            if self.is_moving_complete == True:
                break
        self.is_moving_complete = False

        rospy.sleep(1)

        rospy.loginfo("go straight")
        msg_moving = MovingParam()
        msg_moving.moving_type = 4
        msg_moving.moving_value_angular = 0.0
        msg_moving.moving_value_linear = 0.20
        self.pub_moving.publish(msg_moving)
        while True:
            if self.is_moving_complete == True:
                break
        self.is_moving_complete = False

        rospy.sleep(1)

        rospy.loginfo("go back straight")
        msg_moving = MovingParam()
        msg_moving.moving_type = 5
        msg_moving.moving_value_angular = 0.0
        msg_moving.moving_value_linear = 0.20
        self.pub_moving.publish(msg_moving)
        while True:
            if self.is_moving_complete == True:
                break
        self.is_moving_complete = False

        rospy.sleep(1)

        rospy.loginfo("go right")
        msg_moving = MovingParam()
        msg_moving.moving_type = 3
        msg_moving.moving_value_angular = 90
        msg_moving.moving_value_linear = 0.0
        self.pub_moving.publish(msg_moving)
        while True:
            if self.is_moving_complete == True:
                break
        self.is_moving_complete = False

        rospy.sleep(1)

        rospy.loginfo("go straight")
        msg_moving = MovingParam()
        msg_moving.moving_type = 4
        msg_moving.moving_value_angular = 0.0
        msg_moving.moving_value_linear = 0.9
        self.pub_moving.publish(msg_moving)
        while True:
            if self.is_moving_complete == True:
                break
        self.is_moving_complete = False

        rospy.sleep(1)

        rospy.loginfo("go left")
        msg_moving = MovingParam()
        msg_moving.moving_type = 2
        msg_moving.moving_value_angular = 90
        msg_moving.moving_value_linear = 0.0
        self.pub_moving.publish(msg_moving)
        while True:
            if self.is_moving_complete == True:
                break
        self.is_moving_complete = False

        rospy.sleep(1)

        rospy.loginfo("go straight")
        msg_moving = MovingParam()
        msg_moving.moving_type = 4
        msg_moving.moving_value_angular = 0.0
        msg_moving.moving_value_linear = 0.2
        self.pub_moving.publish(msg_moving)
        while True:
            if self.is_moving_complete == True:
                break
        self.is_moving_complete = False

        rospy.sleep(1)






    def cbParkingOrder(self, order):
        msg_pub_parking_return = UInt8()

        if order.data == self.StepOfParking.parking.value:
            rospy.loginfo("Now motion")
            msg_pub_max_vel = Float64()
            msg_pub_max_vel.data = 0.00
            self.pub_max_vel.publish(msg_pub_max_vel)

            rospy.sleep(1)

            rospy.loginfo("go straight")
            msg_moving = MovingParam()
            msg_moving.moving_type = 4
            msg_moving.moving_value_angular = 0.0
            msg_moving.moving_value_linear = 0.45
            self.pub_moving.publish(msg_moving)
            while True:
                if self.is_moving_complete == True:
                    break
            self.is_moving_complete = False

            rospy.sleep(1)

            rospy.loginfo("go left")
            msg_moving = MovingParam()
            msg_moving.moving_type = 2
            msg_moving.moving_value_angular = 90
            msg_moving.moving_value_linear = 0.0
            self.pub_moving.publish(msg_moving)
            while True:
                if self.is_moving_complete == True:
                    break
            self.is_moving_complete = False

            rospy.sleep(1)

            rospy.loginfo("go straight")
            msg_moving = MovingParam()
            msg_moving.moving_type = 4
            msg_moving.moving_value_angular = 0.0
            msg_moving.moving_value_linear = 1.0
            self.pub_moving.publish(msg_moving)
            while True:
                if self.is_moving_complete == True:
                    break
            self.is_moving_complete = False

            rospy.sleep(1)

            self.start_obstacle_detection = True
            while True:
                if self.is_obstacle_detected_L == True or self.is_obstacle_detected_R == True:
                    break

            if self.is_obstacle_detected_R == False:
                rospy.loginfo("right parking is clear")
                rospy.loginfo("go right")
                msg_moving = MovingParam()
                msg_moving.moving_type = 3
                msg_moving.moving_value_angular = 90
                msg_moving.moving_value_linear = 0.0
                self.pub_moving.publish(msg_moving)
                while True:
                    if self.is_moving_complete == True:
                        break
                self.is_moving_complete = False

                rospy.sleep(1)

                rospy.loginfo("go straight")
                msg_moving = MovingParam()
                msg_moving.moving_type = 4
                msg_moving.moving_value_angular = 0.0
                msg_moving.moving_value_linear = 0.20
                self.pub_moving.publish(msg_moving)
                while True:
                    if self.is_moving_complete == True:
                        break
                self.is_moving_complete = False

                rospy.sleep(1)

                rospy.loginfo("go back straight")
                msg_moving = MovingParam()
                msg_moving.moving_type = 5
                msg_moving.moving_value_angular = 0.0
                msg_moving.moving_value_linear = 0.20
                self.pub_moving.publish(msg_moving)
                while True:
                    if self.is_moving_complete == True:
                        break
                self.is_moving_complete = False

                rospy.sleep(1)

                rospy.loginfo("go right")
                msg_moving = MovingParam()
                msg_moving.moving_type = 3
                msg_moving.moving_value_angular = 90
                msg_moving.moving_value_linear = 0.0
                self.pub_moving.publish(msg_moving)
                while True:
                    if self.is_moving_complete == True:
                        break
                self.is_moving_complete = False

                rospy.sleep(1)

                rospy.loginfo("go straight")
                msg_moving = MovingParam()
                msg_moving.moving_type = 4
                msg_moving.moving_value_angular = 0.0
                msg_moving.moving_value_linear = 0.9
                self.pub_moving.publish(msg_moving)
                while True:
                    if self.is_moving_complete == True:
                        break
                self.is_moving_complete = False

                rospy.sleep(1)

                rospy.loginfo("go left")
                msg_moving = MovingParam()
                msg_moving.moving_type = 2
                msg_moving.moving_value_angular = 90
                msg_moving.moving_value_linear = 0.0
                self.pub_moving.publish(msg_moving)
                while True:
                    if self.is_moving_complete == True:
                        break
                self.is_moving_complete = False

                rospy.sleep(1)

                rospy.loginfo("go straight")
                msg_moving = MovingParam()
                msg_moving.moving_type = 4
                msg_moving.moving_value_angular = 0.0
                msg_moving.moving_value_linear = 0.2
                self.pub_moving.publish(msg_moving)
                while True:
                    if self.is_moving_complete == True:
                        break
                self.is_moving_complete = False

                rospy.sleep(1)

            elif self.is_obstacle_detected_L == False:
                rospy.loginfo("left parking is clear")
                rospy.loginfo("go left")
                msg_moving = MovingParam()
                msg_moving.moving_type = 2
                msg_moving.moving_value_angular = 90
                msg_moving.moving_value_linear = 0.0
                self.pub_moving.publish(msg_moving)
                while True:
                    if self.is_moving_complete == True:
                        break
                self.is_moving_complete = False

                rospy.sleep(1)

                rospy.loginfo("go straight")
                msg_moving = MovingParam()
                msg_moving.moving_type = 4
                msg_moving.moving_value_angular = 0.0
                msg_moving.moving_value_linear = 0.20
                self.pub_moving.publish(msg_moving)
                while True:
                    if self.is_moving_complete == True:
                        break
                self.is_moving_complete = False

                rospy.sleep(1)

                rospy.loginfo("go back straight")
                msg_moving = MovingParam()
                msg_moving.moving_type = 5
                msg_moving.moving_value_angular = 0.0
                msg_moving.moving_value_linear = 0.20
                self.pub_moving.publish(msg_moving)
                while True:
                    if self.is_moving_complete == True:
                        break
                self.is_moving_complete = False

                rospy.sleep(1)

                rospy.loginfo("go left")
                msg_moving = MovingParam()
                msg_moving.moving_type = 2
                msg_moving.moving_value_angular = 90
                msg_moving.moving_value_linear = 0.0
                self.pub_moving.publish(msg_moving)
                while True:
                    if self.is_moving_complete == True:
                        break
                self.is_moving_complete = False

                rospy.sleep(1)

                rospy.loginfo("go straight")
                msg_moving = MovingParam()
                msg_moving.moving_type = 4
                msg_moving.moving_value_angular = 0.0
                msg_moving.moving_value_linear = 1.0
                self.pub_moving.publish(msg_moving)
                while True:
                    if self.is_moving_complete == True:
                        break
                self.is_moving_complete = False

                rospy.sleep(1)

                rospy.loginfo("go left")
                msg_moving = MovingParam()
                msg_moving.moving_type = 2
                msg_moving.moving_value_angular = 90
                msg_moving.moving_value_linear = 0.0
                self.pub_moving.publish(msg_moving)
                while True:
                    if self.is_moving_complete == True:
                        break
                self.is_moving_complete = False

                rospy.sleep(1)

                rospy.loginfo("go straight")
                msg_moving = MovingParam()
                msg_moving.moving_type = 4
                msg_moving.moving_value_angular = 0.0
                msg_moving.moving_value_linear = 0.2
                self.pub_moving.publish(msg_moving)
                while True:
                    if self.is_moving_complete == True:
                        break
                self.is_moving_complete = False

            rospy.loginfo("parking finished")
            msg_pub_parking_return.data = self.StepOfParking.exit.value

        elif order.data == self.StepOfParking.exit.value:
            rospy.loginfo("parking finished")
            msg_pub_parking_return.data = self.StepOfParking.exit.value

        self.pub_parking_return.publish(msg_pub_parking_return)
        rospy.sleep(3)

    def cbScanObstacle(self, scan):
        angle_scan = 30

        scan_start_left = 90 - angle_scan
        scan_end_left = 90 + angle_scan

        scan_start_right = 270 - angle_scan
        scan_end_right = 270 + angle_scan

        threshold_distance = 0.5

        if self.start_obstacle_detection == True:
            for i in range(scan_start_left, scan_end_left):
                if scan.ranges[i] < threshold_distance and scan.ranges[i] > 0.01:
                    self.is_obstacle_detected_L = True
                    rospy.loginfo("left detected")

            for i in range(scan_start_right, scan_end_right):
                if scan.ranges[i] < threshold_distance and scan.ranges[i] > 0.01:
                    self.is_obstacle_detected_R = True
                    rospy.loginfo("right detected")
            self.start_obstacle_detection = False

    def main(self):
        rospy.spin()


if __name__ == '__main__':
    rospy.init_node('detect_parking')
    node = DetectParking()
    node.main()
