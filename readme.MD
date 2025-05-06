cd ~/dev_ws
colcon build

ros2 run vla_x1 topic_jointstate_sub
ros2 run vla_x1 topic_jointcommand_pub
