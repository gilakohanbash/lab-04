#vm_start_chain.py
import rospy
from std_msgs.msg import String

#function to publish messages at a rate of 2 messages per second
def publisher():

#integer num as payload
num = 0
#define a topic to which the messages will be published
message_publisher = rospy.Publisher('gkohanba/ping', int, queue_size=10)

#initialize the Publisher node
#anonymous-True appends random ints at the end of publisher node
rospy.init_node('messagePubNode', anonymous=True)

#publishes at a rate of 2 messages per second
rate = rospy.Rate(2)

#publishes messages indefinetly
while True:
  message = "hello world %s"
  num++
  rospy.loginfo('Published: ' + message)

#add a time.sleep() before publishing
time.sleep(1)
message_publisher.publish(message)
#rate.sleep()

if__name__=='__main__':
try:
  publisher()

#capture the Interrupt signals
except rospy.ROSInterruptException:
  pass
