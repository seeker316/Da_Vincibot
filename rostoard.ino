/*
 * rosserial Servo Control Example with PCA9685 and Int32MultiArray
 *
 * This sketch demonstrates the control of hobby R/C servos
 * using ROS, Arduino with PCA9685 servo controller, and Int32MultiArray
 * 
 * For the full tutorial write-up, visit
 * www.ros.org/wiki/rosserial_arduino_demos
 *
 * For more information on the Arduino Servo Library
 * Checkout:
 * http://www.arduino.cc/en/Reference/Servo
 */

#if (ARDUINO >= 100)
#include <Arduino.h>
#else
#include <WProgram.h>
#endif

#include <Wire.h>          // Include Wire library for I2C communication
#include <Adafruit_PWMServoDriver.h> // Include Adafruit PCA9685 library
#include <ros.h>
#include <std_msgs/Int32MultiArray.h>

ros::NodeHandle nh;

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(); // Create Adafruit PCA9685 servo controller object

void servo_cb(const std_msgs::Int32MultiArray& cmd_msg) {
  if (cmd_msg.data_length >= 5) { // Ensure that the message contains at least 5 elements
    int servoAngles[5]; // Create an array to store servo angles

    for (int i = 0; i < 5; i++) {
      servoAngles[i] = cmd_msg.data[i]; // Extract angles from the message
    }

    // Now you can use the servoAngles array to control your servos as needed
    // Example:
    int pulse0 = map(servoAngles[0], 0, 180, 150, 600);
    int pulse1 = map(servoAngles[1], 0, 180, 150, 600);
    int pulse2 = map(servoAngles[2], 0, 180, 150, 600);
    int pulse3 = map(servoAngles[3], 0, 180, 150, 600);
    int pulse4 = map(servoAngles[4], 0, 180, 150, 600);
    pwm.setPWM(0, 0, pulse0); // Set angle for servo 0
    pwm.setPWM(1, 0, pulse1);
    pwm.setPWM(2, 0, pulse2);
    pwm.setPWM(3, 0, pulse3);
    pwm.setPWM(4, 0, pulse4);

    
    if (servoAngles[0] == 10) {
      digitalWrite(13, HIGH);
      delay(2); // Toggle LED
      digitalWrite(13, LOW);
    }
  }
}

ros::Subscriber<std_msgs::Int32MultiArray> sub("angles", servo_cb);

void setup() {
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
  pwm.begin(); // Initialize PCA9685
  pwm.setPWMFreq(60); // Set the PWM frequency to 60 Hz (adjust as needed)

  // Initialize all servos to position 0 using microstepping with 5 steps
  int servoSteps = 5; // Number of microsteps
  int servoInitialPosition = 0; // Initial position in degrees
  int servoStepSize = 180 / servoSteps; // Calculate the step size

  for (int servoNum = 0; servoNum < 5; servoNum++) {
    int pulseWidth = map(servoInitialPosition, 0, 180, 150, 600); // Map the initial position to pulse width
    pwm.setPWM(servoNum, 0, pulseWidth); // Set the initial pulse width for the servo
    servoInitialPosition += servoStepSize; // Move to the next microstep
  }
}

void loop() {
  nh.spinOnce();
  delay(1);
}
