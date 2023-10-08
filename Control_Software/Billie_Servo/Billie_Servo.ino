#include <TimerOne.h>

int speedpin=5;
int dir=7;
float mspeed;

int setpoint;
int current_pos, j;
int error = 0, derivative = 0, last_error = 0;

float kp = 1;
float ki = 0;
float kd = 0.4;

void setup() {
pinMode(speedpin,OUTPUT);
pinMode(dir,OUTPUT);
pinMode(A0,INPUT);
Serial.begin(9600);
setpoint =150;
//Timer1.initialize(10000000); // 5 seconds (5000000 microseconds)
//Timer1.attachInterrupt(set_loop);
}

void loop() {

current_pos = map(analogRead(A0),0,1023,0,270);
Serial.println(current_pos);
error = setpoint - current_pos;
derivative = error - last_error;

mspeed =((100./270.) * kp * abs(error)) + 80;

if (error < -4) {
  digitalWrite(dir,HIGH);
  analogWrite(speedpin,mspeed); 
//  Serial.println(error);
}

if (error > 4) {
  digitalWrite(dir,LOW);
  analogWrite(speedpin,mspeed);
//  Serial.println(error);
}

if ((error<4) && (error>-4)){
  analogWrite(speedpin,0);
//  Serial.println("OFF");
}
}

void set_loop() {
  if (setpoint == 270){
    setpoint = 0;
    return;
  }
  
  if (setpoint == 0){
    setpoint = 270;
    return;
  }
}
