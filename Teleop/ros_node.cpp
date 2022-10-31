#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("Message received: [%s]", msg->data.c_str());
}

struct Speed{
    double angular=0;
    double linear=0;
};

int main(int argc, char **argv)
{
  ros::init(argc, argv, "listener");

  ros::NodeHandle n;

  ros::Subscriber sub = n.subscribe("/topic", 1883, chatterCallback);
  ros::spin();

  ros::Publisher chatter_pub = n.advertise<std_msgs::String>("/cmd_web", 1883);
  ros::Rate loop_rate(10);
  int count = 0;
  Speed speed;
  while (ros::ok())
  {
    std_msgs::String msg;
    std::stringstream ss;
    ss << speed.linear << "/" << speed.angular;
    msg.data = ss.str();
    ROS_INFO("%s", msg.data.c_str());
    chatter_pub.publish(msg);
    ros::spinOnce();
    loop_rate.sleep(); 
    speed.angular+=0.1;
    speed.linear-=0.05;
  }

  return 0;
}
