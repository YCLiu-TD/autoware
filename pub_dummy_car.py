# Ustage: $ python3 pub_dummy_car.py
import rclpy
from rclpy.node import Node
from tier4_simulation_msgs.msg import DummyObject
from builtin_interfaces.msg import Time
from geometry_msgs.msg import PoseWithCovariance, TwistWithCovariance, AccelWithCovariance
from unique_identifier_msgs.msg import UUID

class DummyObjectPublisher(Node):
    def __init__(self):
        super().__init__('dummy_object_publisher')
        self.publisher_ = self.create_publisher(DummyObject, '/simulation/dummy_perception_publisher/object_info', 10)
        self.get_logger().info("DummyObject Publisher Initialized")

    def publish_dummy_object(self, data):
        # create message
        obj = DummyObject()
        obj.header.stamp = self.get_clock().now().to_msg()
        obj.header.frame_id = 'map'

        # Header
        obj.header.frame_id = 'map'

        # UUID (id)
        obj.id.uuid = [
            81, 153, 240, 246, 208, 101, 196, 190, 55, 76, 141, 118, 122, 78, 81, 24
        ]

        # Classification
        obj.classification.label = data["classification_label"]
        obj.classification.probability = data["classification_probability"]

        # Shape
        obj.shape.type = 0
        obj.shape.dimensions.x = data["shape_dimensions"][0]
        obj.shape.dimensions.y = data["shape_dimensions"][1]
        obj.shape.dimensions.z = data["shape_dimensions"][2]

        # Initial State
        obj.initial_state.pose_covariance.pose.position.x = data["position"][0]
        obj.initial_state.pose_covariance.pose.position.y = data["position"][1]
        obj.initial_state.pose_covariance.pose.position.z = data["position"][2]
        obj.initial_state.pose_covariance.pose.orientation.x = data["orientation"][0]
        obj.initial_state.pose_covariance.pose.orientation.y = data["orientation"][1]
        obj.initial_state.pose_covariance.pose.orientation.z = data["orientation"][2]
        obj.initial_state.pose_covariance.pose.orientation.w = data["orientation"][3]
        obj.initial_state.twist_covariance.twist.linear.x = data["velocity"]
        obj.initial_state.twist_covariance.twist.linear.y = 0.0
        obj.initial_state.twist_covariance.twist.linear.z = 0.0
        obj.initial_state.accel_covariance.accel.linear.x = data["acceleration"]
        obj.initial_state.accel_covariance.accel.linear.y = 0.0
        obj.initial_state.accel_covariance.accel.linear.z = 0.0

        # Action
        obj.action = 0

        # publishers
        self.publisher_.publish(obj)
        self.get_logger().info(f"Published DummyObject message: {obj}")


def main(args=None):
    rclpy.init(args=args)
    node = DummyObjectPublisher()

    # dummy objects data
    obj_data = [
        {
            "position": [81573.8125, 50085.46484375, 0.0],
            "orientation": [0.0, 0.0, 0.06662573601413951, 0.9977780370907019],
            "classification_label": 1,
            "classification_probability": 1.0,
            "shape_dimensions": [4.0, 1.8, 2.0],
            "velocity": 0.0,
            "acceleration": 0.0
        },
        {
            "position": [81572.0625, 50094.68359375, 0.0],
            "orientation": [0.0, 0.0, 0.07126037557074487, 0.9974577479139236],
            "classification_label": 1,
            "classification_probability": 1.0,
            "shape_dimensions": [4.0, 1.8, 2.0],
            "velocity": 0.0,
            "acceleration": 0.0
        },
        {
            "position": [81585.28125, 50096.96484375, 0.0],
            "orientation": [0.0, 0.0, 0.9966837102246545, -0.08137310226860586],
            "classification_label": 1,
            "classification_probability": 1.0,
            "shape_dimensions": [4.0, 1.8, 2.0],
            "velocity": 0.0,
            "acceleration": 0.0
        },
        {
            "position": [81586.109375, 50090.703125, 0.0],
            "orientation": [0.0, 0.0, 0.9957801928910253, -0.09177040615532046],
            "classification_label": 1,
            "classification_probability": 1.0,
            "shape_dimensions": [4.0, 1.8, 2.0],
            "velocity": 0.0,
            "acceleration": 0.0
        },
        {
            "position": [81586.796875, 50087.453125, 0.0],
            "orientation": [0.0, 0.0, 0.9959109910870148, -0.09033990166078341],
            "classification_label": 1,
            "classification_probability": 1.0,
            "shape_dimensions": [4.0, 1.8, 2.0],
            "velocity": 0.0,
            "acceleration": 0.0
        },
        {
            "position": [81568.640625, 50119.6640625, 0.0],
            "orientation": [0.0, 0.0, 0.07742081638064648, 0.9969985041066782],
            "classification_label": 1,
            "classification_probability": 1.0,
            "shape_dimensions": [4.0, 1.8, 2.0],
            "velocity": 0.0,
            "acceleration": 0.0
        },
        {
            "position": [81568.1328125, 50122.73046875, 0.0],
            "orientation": [0.0, 0.0, 0.05530038643826718, 0.998469762816971],
            "classification_label": 1,
            "classification_probability": 1.0,
            "shape_dimensions": [4.0, 1.8, 2.0],
            "velocity": 0.0,
            "acceleration": 0.0
        },
        {
            "position": [81567.4453125, 50125.7421875, 0.0],
            "orientation": [0.0, 0.0, 0.05353205976520364, 0.9985661312989214],
            "classification_label": 1,
            "classification_probability": 1.0,
            "shape_dimensions": [4.0, 1.8, 2.0],
            "velocity": 0.0,
            "acceleration": 0.0
        },
        {
            "position": [81580.3515625, 50127.8359375, 0.0],
            "orientation": [0.0, 0.0, 0.9482940982044005, -0.3173929793027925],
            "classification_label": 1,
            "classification_probability": 1.0,
            "shape_dimensions": [4.0, 1.8, 2.0],
            "velocity": 0.0,
            "acceleration": 0.0
        },
        {
            "position": [81581.2890625, 50119.7578125, 0.0],
            "orientation": [0.0, 0.0, 0.9248781692644066, -0.3802635559952066],
            "classification_label": 1,
            "classification_probability": 1.0,
            "shape_dimensions": [4.0, 1.8, 2.0],
            "velocity": 0.0,
            "acceleration": 0.0
        }
    ]

    try:
        for data in obj_data:
            node.publish_dummy_object(data)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
