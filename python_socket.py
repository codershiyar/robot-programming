# Import the socket library for network communication
# استيراد مكتبة السوكيت للتواصل الشبكي

# Coder Shiyar 05-04-2024 

import socket

# The IP address of the robot controller on the network
# عنوان IP لوحدة تحكم الروبوت على الشبكة
host = "192.168.0.5"
# The port number that the robot controller is listening on
# رقم المنفذ الذي تستمع إليه وحدة تحكم الروبوت
port = 30002

# Create a socket object.
# إنشاء كائن سوكيت
# AF_INET specifies that we'll use IPv4 addresses.
# SOCK_STREAM indicates that this will be a TCP socket.
# AF_INET يحدد أننا سنستخدم عناوين IPv4
# SOCK_STREAM يشير إلى أن هذا سيكون سوكيت TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the robot controller at the specified host and port
    # الاتصال بوحدة تحكم الروبوت على العنوان والمنفذ المحددين
    s.connect((host, port))
    print("Successfully connected to the robot controller.")
    # تم الاتصال بنجاح بوحدة تحكم الروبوت

    # Command to move the robot.
    # This command moves the robot to a predefined position with specified acceleration (a) and velocity (v).
    # أمر لتحريك الروبوت
    # هذا الأمر يحرك الروبوت إلى موقع محدد مسبقاً مع تسارع وسرعة محددين
    command = b"movej(p[0.233946, 0.0837416, 0.967393, -1.89686, 1.81847, -0.622923], a=1.0, v=0.5)\n"
    
    # Send the command to the robot controller.
    # إرسال الأمر إلى وحدة تحكم الروبوت
    s.send(command)
    print("Command sent to the robot controller.")
    # تم إرسال الأمر إلى وحدة تحكم الروبوت

    # Wait to receive data from the robot controller.
    # 1024 bytes is the maximum amount of data to be received at once.
    # الانتظار لاستقبال البيانات من وحدة تحكم الروبوت
    # 1024 بايت هو الحد الأقصى لكمية البيانات التي يمكن استقبالها دفعة واحدة
    data = s.recv(1024)
    print("Received data from the robot controller:", data)
    # تم استقبال البيانات من وحدة تحكم الروبوت

finally:
    # Always close the socket connection when done to free up resources.
    # يجب دائماً إغلاق اتصال السوكيت بعد الانتهاء لتحرير الموارد
    s.close()
    print("Connection closed.")
    # تم إغلاق الاتصال
