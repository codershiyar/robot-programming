from urx import Robot
import time

# Created by Coder Shiyar | https://codershiyar.com 
# Netherlands Kurdistan | 25, 
def connect_to_robot(robot_ip):
    """
    Connects to the UR10 robot.

    Parameters:
        robot_ip (str): The IP address of the robot.

    Returns:
        Robot: The connected robot object.
    """
    robot = Robot(robot_ip)
    return robot

def move_to_position(robot, target_pose, acceleration=0.5, velocity=0.5):
    """
    Moves the robot to a specified position.

    Parameters:
        robot (Robot): The connected robot object.
        target_pose (tuple): Target position and orientation (X, Y, Z, RX, RY, RZ).
        acceleration (float): Acceleration value for the movement (default: 0.5).
        velocity (float): Velocity value for the movement (default: 0.5).
    """
    robot.movej(target_pose, acc=acceleration, vel=velocity)

def stop_robot(robot):
    """
    Stops the movement of the robot.

    Parameters:
        robot (Robot): The connected robot object.
    """
    robot.stopl()

def disconnect_robot(robot):
    """
    Disconnects from the robot.

    Parameters:
        robot (Robot): The connected robot object.
    """
    robot.close()

def rotate_robot(robot, rx_offset, ry_offset, acceleration=0.5, velocity=0.5):
    """
    Rotates the robot around its fixed position by adjusting RX and RY angles.

    Parameters:
        robot (Robot): The connected robot object.
        rx_offset (float): Offset value for RX angle (in radians).
        ry_offset (float): Offset value for RY angle (in radians).
        acceleration (float): Acceleration value for the movement (default: 0.5).
        velocity (float): Velocity value for the movement (default: 0.5).
    """
    current_pose = robot.getl()
    new_orientation = (current_pose[3], current_pose[4] + rx_offset, current_pose[5] + ry_offset)
    robot.movel(current_pose[0:3] + new_orientation, acc=acceleration, vel=velocity)

if __name__ == "__main__":
    # Example usage:
    robot_ip_address = "192.168.1.100"  # Replace with the actual IP address of your UR10 robot

    # Connect to the robot
    ur10_robot = connect_to_robot(robot_ip_address)

    # Example target position (X, Y, Z, RX, RY, RZ)
    target_position = (0.5, 0.5, 0.5, 0, 0, 0)

    # Move to the target position
    move_to_position(ur10_robot, target_position)

    # Pause for safety
    time.sleep(2)

    # Stop the robot
    stop_robot(ur10_robot)

    # Rotate the robot around its fixed position by adjusting RX and RY angles
    rotate_robot(ur10_robot, rx_offset=0.1, ry_offset=0.1)

    # Stop the robot
    stop_robot(ur10_robot)

    # Disconnect from the robot
    disconnect_robot(ur10_robot)




# Simple example to move robot to the target position.

# from urx import Robot

# def main(robot_ip):
#     # Connect to the robot
#     robot = Robot(robot_ip)

#     # Set a target pose (position and orientation)
#     target_pose = (0.5, 0.5, 0.5, 0, 0, 0)  # Example target pose (X, Y, Z, RX, RY, RZ)

#     # Move to the target pose
#     robot.movej(target_pose, acc=0.5, vel=0.5)  # MoveJ command (joint movement)

#     # Close the connection
#     robot.close()

# if __name__ == "__main__":
#     # Specify the IP address of your UR10 robot
#     robot_ip_address = "192.168.1.100"  # Example IP address, replace with your robot's IP
#     main(robot_ip_address)




# maybe you need this for later
# import RPi.GPIO as GPIO

# Setup GPIO pin
# button_pin = 18
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

 # if GPIO.input(button_pin) == GPIO.LOW:
 #           print("do something")



# extra: 
    # # Get the current pose of the robot
    # current_pose = robot.get_pose() 

    # # Extract rotation vector and position from the pose
    # pattern = r"[-+]?\d*\.\d+|\d+"
    # numbers = [float(num) for num in re.findall(pattern, str(current_pose))]
    # rotation_vector = tuple(numbers[:3])
    # position = tuple(numbers[3:6])
    # print("Rotation vector:", rotation_vector)
    # print("Position:", position)
    
    # # Convert mm to meters for position
    # px, py, pz = [num * 1000 for num in position]
    # # Assign rotational components
    # rx, ry, rz =rotation_vector
    # print((px, py, pz, rx, ry, rz))
