import rclpy
from rclpy.node import Node
from vla_msg.msg import JointCommand  # 导入自定义消息类型
import redis
import json
import time

"""
从redis list 'joint_cmd' 得到关节数据并写到ros2 topic 'joint_cmd'
"""
class JointCommandPublisher(Node):

    def __init__(self):
        super().__init__('joint_command_publisher')

        # 创建发布者
        self.publisher_ = self.create_publisher(JointCommand, 'joint_cmd', 10)

        # 初始化 Redis 客户端
        self.redis_client = redis.StrictRedis(host='192.168.110.91', port=6379, db=0)

    def publish_from_redis(self):
        try:
            # 从 Redis list 右侧左弹出一个值
            _, data = self.redis_client.blpop('joint_cmd')
            # 数据是 JSON 格式的字符串
            joint_data = json.loads(data.decode('utf-8'))
            # 构造 JointCommand 消息
            msg = JointCommand()
            msg.name = joint_data.get("name", [])
            msg.position = joint_data.get("position", [])
            msg.velocity = joint_data.get("velocity", [])
            msg.effort = joint_data.get("effort", [])
            msg.stiffness = joint_data.get("stiffness", [])
            msg.damping = joint_data.get("damping", [])

            # 发布消息
            self.publisher_.publish(msg)
            self.get_logger().info(f'Published joint command: {msg}')
        except Exception as e:
            self.get_logger().error(f"Error processing Redis data: {e}")

def main(args=None):
    rclpy.init()
    node = JointCommandPublisher()
    try:
        while rclpy.ok():
            node.publish_from_redis()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
