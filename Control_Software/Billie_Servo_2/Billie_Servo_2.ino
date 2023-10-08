#include <TimerOne.h>

int speedpin_0 = 5, speedpin_1 = 6;
int dir_0 = 7, dir_1 = 8;
float mspeed_0, mspeed_1 ;

int setpoint_0 = 200, setpoint_1 = 100;
int current_pos_0, current_pos_1;
int error_0, error_1;

float kp = 1;
float ki = 0;
float kd = 0.4;

void setup() {
  
pinMode(speedpin_0,OUTPUT);
pinMode(speedpin_1,OUTPUT);
pinMode(dir_0,OUTPUT);
pinMode(dir_1,OUTPUT);
pinMode(A0,INPUT);
pinMode(A1,INPUT);

Serial.begin(9600);
//Timer1.initialize(20000000); // 5 seconds (5000000 microseconds)
//Timer1.attachInterrupt(set_loop);

}

void loop() {

current_pos_0 = map(analogRead(A0),0,1023,0,270);
current_pos_1 = map(analogRead(A1),0,1023,0,270);
//Serial.println(current_pos_0);
//Serial.println(current_pos_1);

error_0 = setpoint_0 - current_pos_0;
error_1 = setpoint_1 - current_pos_1;
//derivative = error - last_error;

mspeed_0 =((100./270.) * kp * abs(error_0)) + 80;
mspeed_1 =((100./270.) * kp * abs(error_1)) + 80;

// Shoulder Yaw Joint
if (error_0 < -2) {
  digitalWrite(dir_0,HIGH);
  analogWrite(speedpin_0,mspeed_0); 
}

if (error_0 > 2) {
  digitalWrite(dir_0,LOW);
  analogWrite(speedpin_0,mspeed_0);
}

if ((error_0 < 2) && (error_0 > -2)){
  analogWrite(speedpin_0,0);
}

// Shoulder Pitch Joint

if (error_1 < -2) {
  digitalWrite(dir_1,HIGH);
  analogWrite(speedpin_1,mspeed_1); 
}

if (error_1 > 2) {
  digitalWrite(dir_1,LOW);
  analogWrite(speedpin_1,mspeed_1);
}

if ((error_1 < 2) && (error_1 > -2)){
  analogWrite(speedpin_1,0);
}
}

void set_loop() {
  if (setpoint_0 == 200){
    setpoint_0 = 100;
    setpoint_1 = 200;
    return;
  }
  
  if (setpoint_0 == 100){
    setpoint_0 = 200;
    setpoint_1 = 100;
    return;
  }
}
