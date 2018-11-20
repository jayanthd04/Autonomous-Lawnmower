# Autonomous-Lawnmower
In this project, I attempted to and am still trying to create an autonomous lawnmower. I started out by creating my own robot from scratch with spare wood and electrical materials. I then upgraded by using an existing robot with it's own motherboard and replaced it with a raspeberry pi. 

# Prerequisites
To get started, all that is required is a simple robot with two motors and castor wheels for support, any motor controller, and a battery. 
# Installing(assuming the user has a pre-existing robot built and uses an L298N motor driver)
1. Begin by connecting the positive end of the left motor on the robot to output1 and the negative end to output2.
2. Repeat step 1 for the right motor on outputs 3 and 4. 
3. Connect the positive end of a 12v battery to the 12v terminal on the motor controller. 
4. Connect the negative end of the 12v battery to the ground terminal on the motor controller.
5. Connect the ENA pin to any 5v IO pin on the raspberry pi. 
6. Connect the IN1 to GPIO pin 14 on the raspberry pi.
7. Connect the IN2 to GPIO pin 15 on the rapsberry pi.
8. Connect the ENB pin to another 5v IO pin on the raspberry pi.
9. Connect the IN3 to GPIO pin 23 on the raspberry pi.
10. Connect the IN4 to GPIO pin 24 on the raspberry pi.
11. Test the polarity of the motor by running the following command on the terminal
    echo 1 > /sys/class/gpio/gpio14/value
12. If the Left motor on the robot rotates clockwise, then the polarity is correct. If the left motor is rotating counter clockwise, then reverse the terminals on outputs 1 and 2
13. Repeat steps 11 and 12 for the right motor by replacing the IO pin value to 23 
    echo 1 > /sys/class/gpio/gpio23/value
# Running the tests
To begin test the code, go to the motor.py file and call the directional methods to give the robot directions. To run the code, type the following command in terminal ".motor.py".
