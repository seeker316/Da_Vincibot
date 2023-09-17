int speedpin=3;
int dir1=4;
int dir2=2;
float mspeed;

int setpoint = 0;
int current_pos;
int error;

void setup() {

pinMode(speedpin,OUTPUT);
pinMode(dir1,OUTPUT);
pinMode(dir2,OUTPUT);
pinMode(A1,INPUT);
Serial.begin(9600);
}

void loop() {

current_pos = map(analogRead(A1),0,1023,0,270);
//Serial.println(current_pos);
error = setpoint - current_pos;

if (error < -5) {
  digitalWrite(dir1,HIGH);
  digitalWrite(dir2,LOW);
//  mspeed =((255./270.) * 1 * abs(error)) + 100;
  analogWrite(speedpin,250); 
  Serial.println(error);
}

if (error > 5) {
  digitalWrite(dir1,LOW);
  digitalWrite(dir2,HIGH);
//  mspeed =((255./270.) * 1 * abs(error)) + 100;
  analogWrite(speedpin,250);
  Serial.println(error);
}

if ((error<5) && (error>-5)){
  digitalWrite(dir1,LOW);
  digitalWrite(dir2,LOW);
  Serial.println("OFF");
}
}
