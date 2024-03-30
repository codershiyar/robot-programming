# Script to Control Universal Robots by Python | Engineer Coder Shiyar
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

[git clone https://github.com/codershiyar/ur10-python-control.git](https://github.com/codershiyar/ur10-python-control)https://github.com/codershiyar/ur10-python-control

2. Navigate to the repository directory:

cd ur10-python-control

3. Open the `ur10_control.py` file and replace `"192.168.1.100"` with the IP address of your UR10 robot.

4: Install 
- `pip install urx `
- `pip install RPi.GPIO`

https://pypi.org/project/urx/0.9.0/
https://pypi.org/project/RPi.GPIO/ 

5. Run the script:

python ur10_control.py

This will connect to the robot, move it to a specified position, pause for safety, stop the robot, and disconnect from it.

## Extra:
In the context of robotics, especially with UR robots, a pose typically consists of 6 components: [x, y, z, rx, ry, rz].

### x, y, z: These represent the position of the robot end-effector in Cartesian coordinates, typically in meters. They specify the end-effector's location in space with respect to the robot's base frame.

- x: movement left and right
- y: movement forward and backward
- z: movement up and down
### rx, ry, rz: These represent the orientation of the robot end-effector in terms of rotation around the Cartesian axes, expressed in radians. They define the orientation of the end-effector.
- rx: rotation around the x-axis (roll)
- ry: rotation around the y-axis (pitch)
- rz: rotation around the z-axis (yaw)

## Customization

You can customize the script by modifying the target position in the `ur10_control.py` file. Additionally, you can adjust the acceleration and velocity parameters for the movement.

Replace "192.168.1.100" in the Python script and the README.md file with the actual IP address of your UR10 robot.

# سكريبت للتحكم بروبوت Universal باستخدام Python | مهندس البرمجة شيار

هذا المستودع يوفر سكريبت Python بسيط (ur10_control.py) للتحكم في روبوت UR10 باستخدام مكتبة URX. يتيح السكريبت للمستخدمين الاتصال بروبوت UR10 وتحريكه إلى موقع محدد وتدويره حول موقعه الثابت وأداء عمليات أساسية أخرى.

## الشروط المسبقة

قبل تشغيل السكريبت، تأكد من وجود الآتي:

- Python مثبت على نظامك
- تثبيت مكتبة `urx` (يمكن تثبيتها عبر pip: `pip install urx`)
- عنوان IP لروبوت UR10 الخاص بك

## الاستخدام

1. استنسخ هذا المستودع إلى جهازك المحلي:

git clone https://github.com/codershiyar/ur10-python-control.git


2. انتقل إلى دليل المستودع:

cd ur10-python-control


3. افتح ملف `ur10_control.py` واستبدل `"192.168.1.100"` بعنوان IP الخاص بروبوت UR10 الخاص بك.

4. قم بالتثبيت:
   - `pip install urx`
   - `pip install RPi.GPIO`

5. قم بتشغيل السكريبت:

python ur10_control.py


سيتصل هذا بالروبوت، وسيقوم بتحريكه إلى موقع محدد، ثم يتوقف لأغراض السلامة، ويتوقف عن العمل، ثم يفصل الاتصال من الروبوت.

## إضافي:

في سياق الروبوتيات، خاصة مع الروبوتات UR، تتكون المواقف عادة من 6 مكونات: [x، y، z، rx، ry، rz].

### x، y، z:
تمثل هذه المكونات موقع نهاية الروبوت بالإحداثيات الديكارتية، عادة بالأمتار. تحدد موقع نهاية الروبوت في الفضاء بالنسبة لإطار قاعدة الروبوت.

- x: حركة يسار ويمين
- y: حركة إلى الأمام والخلف
- z: حركة أعلى وأسفل

### rx، ry، rz:
تمثل هذه المكونات توجيه نهاية الروبوت من حيث الدوران حول المحاور الديكارتية، بالراديان. تعرف توجيه نهاية الروبوت.

- rx: دوران حول محور x (دوران)
- ry: دوران حول محور y (ميل)
- rz: دوران حول محور z (ياو)

robot.movej((x, y, z, rx, ry, rz), acc=0.5, vel=0.5)

- movej يستخدم لتحريك الروبوت
- "target_pose (x, y, z, rx, ry, rz)": اجباري

هذا هو المعلمة التي تحدد الموقع الذي يجب على الروبوت الوصول إليه. يتم تحديدها عادة باستخدام إحداثيات مفصلية (Joint coordinates) أو إحداثيات كارتيزية (Cartesian coordinates)، اعتمادًا على نوعية الروبوت ونظام التحكم الذي يُستخدم.
- "acc" (التسارع): اختياري

هذه القيمة تحدد معدل التسارع الذي يستخدمه الروبوت أثناء الحركة. وتشير إلى كمية التغير في سرعة الروبوت خلال الحركة. قيمة أعلى تعني تسارع أكبر وحركة أسرع، بينما قيمة أقل تعني تسارع أقل وحركة أبطأ.
- "vel" (السرعة): اختياري

هذه القيمة تحدد سرعة الروبوت أثناء الحركة. وتعبر عن السرعة القصوى التي يمكن للروبوت أن يتحرك بها أثناء الحركة نحو الموقع المحدد. قيمة أعلى تعني سرعة أكبر للروبوت، بينما قيمة أقل تعني سرعة أبطأ.

## التخصيص

يمكنك تخصيص السكريبت عن طريق تعديل الموقع المستهدف في ملف `ur10_control.py`. بالإضافة إلى ذلك، يمكنك ضبط معلمات الوتيرة والتسارع للحركة.

استبدل "192.168.1.100" في السكريبت Python وملف README.md بعنوان IP الفعلي لروبوت UR10 الخاص بك.
