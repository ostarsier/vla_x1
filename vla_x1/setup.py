from setuptools import find_packages, setup
from glob import glob

package_name = 'vla_x1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/' + package_name, ['package.xml']),
        # 添加这一行，让ROS2识别msg目录下的消息
        ('share/' + package_name + '/msg', glob('vla_x1/msg/*.msg')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yonsvm',
    maintainer_email='yonsvm@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'topic_jointcommand_pub = vla_x1.topic_jointcommand_pub:main',
            'topic_jointstate_sub = vla_x1.topic_jointstate_sub:main',
            'topic_helloworld_sub = vla_x1.topic_helloworld_sub:main',
        ],
    },
)
