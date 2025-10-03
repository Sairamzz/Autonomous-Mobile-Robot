import rclpy
from tf2_ros import TransformListener
from geometry_msgs.msg import TransformStamped

def main():
    rclpy.init()

    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer, node=rclpy.create_node('tf_listener'))

    try:
        while True:
            # Attempt to lookup transform from "base_link" to "left_wheel"
            try:
                transform = tf_buffer.lookup_transform("base_link", "left_wheel", rclpy.time.Time())
                print("Transform from 'base_link' to 'left_wheel':", transform)
            except Exception as e:
                print("Error:", e)
            
            # Attempt to lookup transform from "base_link" to "right_wheel"
            try:
                transform = tf_buffer.lookup_transform("base_link", "right_wheel", rclpy.time.Time())
                print("Transform from 'base_link' to 'right_wheel':", transform)
            except Exception as e:
                print("Error:", e)

            rclpy.spin_once(tf_listener.node)
            
    except KeyboardInterrupt:
        pass

    tf_listener.destroy()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
