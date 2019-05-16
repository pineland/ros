#!/usr/bin/env python

from rospy_tutorials_parameter.srv import *
import rospy

PLUS = 1
MINUS = 2
MULTIPLICATION = 3
DIVISION = 4

g_operation = PLUS

def handle_four_operations(req):
    g_operation = rospy.get_param('calculation_method')
    rospy.loginfo('currently g_operation is %i', g_operation)
    if g_operation == PLUS:
        computed_result = req.a + req.b
    elif g_operation == MINUS:
        computed_result = req.a - req.b
    elif g_operation == MULTIPLICATION:
        computed_result = req.a * req.b
    elif g_operation == DIVISION:
        computed_result = req.a / req.b
    else:
        print "Error g_operation!!"
    return FourOperationsResponse(computed_result)

def four_operations_server():
    rospy.init_node('four_operations_server')
    rospy.set_param('calculation_method', PLUS)
    s = rospy.Service('four_operations', FourOperations, handle_four_operations)
    print "Ready to operate.."
    r = rospy.Rate(10)
    rospy.spin()    # trigger callback
    r.sleep()

if __name__ == "__main__":
    four_operations_server()
