
cd /home/yonsvm/code/robot-infer
cd build/
./run_sim.sh

---
redis-cli -h 192.168.110.91

---
cd ~/dev_ws
colcon build

ros2 run vla_x1 topic_jointstate_sub
ros2 run vla_x1 topic_jointcommand_pub


---





