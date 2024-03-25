# ur10-python-control
This repository provides a Python script (ur10_control.py) for controlling a UR10 robot using the URX library. The script allows users to connect to a UR10 robot, move it to a specified position, rotate it around its fixed position, and perform other basic operations.

# Controlling UR10 Robot Using Python

This repository provides a simple Python script to control a UR10 robot. The script utilizes the `urx` library for communication with the robot over the network.

## Prerequisites

Before running the script, ensure that you have the following:

- Python installed on your system
- The `urx` library installed (can be installed via pip: `pip install urx`)
- The IP address of your UR10 robot

## Usage

1. Clone this repository to your local machine:

[git clone https://github.com/yourusername/ur10-python-control.git](https://github.com/codershiyar/ur10-python-control)https://github.com/codershiyar/ur10-python-control

2. Navigate to the repository directory:

cd ur10-python-control

3. Open the `ur10_control.py` file and replace `"192.168.1.100"` with the IP address of your UR10 robot.

4. Run the script:

python ur10_control.py

This will connect to the robot, move it to a specified position, pause for safety, stop the robot, and disconnect from it.

## Extra:
In the context of robotics, especially with UR robots, a pose typically consists of 6 components: [x, y, z, rx, ry, rz].

x, y, z: These represent the position of the robot end-effector in Cartesian coordinates, typically in meters. They specify the end-effector's location in space with respect to the robot's base frame.

x: movement left and right
y: movement forward and backward
z: movement up and down
rx, ry, rz: These represent the orientation of the robot end-effector in terms of rotation around the Cartesian axes, expressed in radians. They define the orientation of the end-effector.

rx: rotation around the x-axis (roll)
ry: rotation around the y-axis (pitch)
rz: rotation around the z-axis (yaw)

## Customization

You can customize the script by modifying the target position in the `ur10_control.py` file. Additionally, you can adjust the acceleration and velocity parameters for the movement.

Replace "192.168.1.100" in the Python script and the README.md file with the actual IP address of your UR10 robot.

