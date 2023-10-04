#include <Wire.h>          // Include Wire library for I2C communication
#include <Adafruit_PWMServoDriver.h> // Include Adafruit PCA9685 library
#include <ros.h>
#include <std_msgs/Int32MultiArray.h>

ros::NodeHandle nh;


Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();


int speedpin_0 = 5, speedpin_1 = 6;
int dir_0 = 7, dir_1 = 8;
float mspeed_0, mspeed_1 ;

int setpoint_0, setpoint_1;
int current_pos_0, current_pos_1;
int error_0, error_1;

float kp = 1;
float ki = 0;
float kd = 0.4;

void servo_cb(const std_msgs::Int32MultiArray& cmd_msg) {
  if (cmd_msg.data_length >= 5) { // Ensure that the message contains at least 5 elements
    int angles[5]; // Create an array to store servo angles

    for (int i = 0; i < 5; i++) {
      angles[i] = cmd_msg.data[i]; // Extract angles from the message
    }
    
    angles[0] = setpoint_0;            // Shoulder yaw joint
 
    angles[1] = setpoint_1;            // Shoulder pitch joint

    control_loop(setpoint_0,setpoint_1);
    
    step_angle(0,angles[2]);           // Elbow joint
    step_angle(1,(180 - angles[2]));
    
    step_angle(2,angles[3]);           // Wrist yaw joint
    
    step_angle(3,angles[4]);           // Wrist pitch joint
    step_angle(4,(180 - angles[4]));
    }
  }

ros::Subscriber<std_msgs::Int32MultiArray> sub("angles", servo_cb);

void setup() {

nh.initNode();
nh.subscribe(sub);

pinMode(speedpin_0,OUTPUT);
pinMode(speedpin_1,OUTPUT);
pinMode(dir_0,OUTPUT);
pinMode(dir_1,OUTPUT);
pinMode(A0,INPUT);
pinMode(A1,INPUT);

pwm.begin();
pwm.setPWMFreq(50);

set_angle(90);
}

void loop() {
  nh.spinOnce();
  delay(1);
}

short set_angle(short angle) {
  short  pulse_count = map(angle, 0, 180, 112, 512);
  pwm.setPWM(0,0,pulse_count);
  pwm.setPWM(1,0,pulse_count);
  pwm.setPWM(2,0,pulse_count);
  pwm.setPWM(3,0,pulse_count);
  pwm.setPWM(4,0,pulse_count);
}

short step_angle(short motor, short angle) {
  short  pulse_count = map(angle, 0, 180, 112, 512);
  pwm.setPWM(motor,0,pulse_count); 
}

void control_loop(short setpoint_0, short setpoint_1) {

// Shoulder Yaw Joint
if (error_0 < -5) {
  digitalWrite(dir_0,HIGH);
  analogWrite(speedpin_0,mspeed_0); 
}

if (error_0 > 5) {
  digitalWrite(dir_0,LOW);
  analogWrite(speedpin_0,mspeed_0);
}

if ((error_0 < 5) && (error_0 > -5)){
  analogWrite(speedpin_0,0);
}

// Shoulder Pitch Joint

if (error_1 < -5) {
  digitalWrite(dir_1,HIGH);
  analogWrite(speedpin_1,mspeed_1); 
}

if (error_1 > 5) {
  digitalWrite(dir_1,LOW);
  analogWrite(speedpin_1,mspeed_1);
}

if ((error_1 < 5) && (error_1 > -5)){
  analogWrite(speedpin_1,0);
}
}
