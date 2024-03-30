from urx import Robot
robot = Robot('192.168.0.5')
current_position = robot.getj()
x, y, z, rx, ry, rz = current_position[:6]

robot.movej( (x+0.2, y, z, rx, ry, rz))