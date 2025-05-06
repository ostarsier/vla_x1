import rclpy                      # ROS2 Python接口库
from rclpy.node   import Node     # ROS2 节点类
from std_msgs.msg import String   # ROS2标准定义的String消息
from sensor_msgs.msg import JointState
import redis
import pickle  # 添加这一行用于序列化

"""
从 ros2 topic 'joint_states' 获取关节数据后, 写到redis key 'joint_states'
"""
class SubscriberNode(Node):

    def __init__(self, name):
        super().__init__(name)                             # ROS2节点父类初始化
        self.sub = self.create_subscription(
            JointState, "joint_states", self.listener_callback, 10) # 创建订阅者对象（消息类型、话题名、订阅者回调函数、队列长度）
        self.redis_client = redis.StrictRedis(host='192.168.110.91', port=6379, db=0)

    def listener_callback(self, msg):                      # 创建回调函数，执行收到话题消息后对数据的处理
        joint_states = pickle.dumps(msg)
        self.redis_client.set('joint_states', joint_states)
        self.get_logger().info('I heard: "%s"' % msg) # 输出日志信息，提示订阅收到的话题消息

def main(args=None):                               # ROS2节点主入口main函数
    rclpy.init(args=args)                          # ROS2 Python接口初始化
    node = SubscriberNode("topic_jointstate_sub")  # 创建ROS2节点对象并进行初始化
    rclpy.spin(node)                               # 循环等待ROS2退出
    node.destroy_node()                            # 销毁节点对象
    rclpy.shutdown()                               # 关闭ROS2 Python接口