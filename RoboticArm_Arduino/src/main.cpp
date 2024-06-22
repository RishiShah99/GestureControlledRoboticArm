#include <Arduino.h>
#include <Servo.h>

#define numOfValsRec 5
#define digitsPerValRec 1

Servo servoThumb;
Servo servoIndex;
Servo servoMiddle;
Servo servoRing;
Servo servoPinky;

int valsRec[numOfValsRec];
int stringLength = numOfValsRec * digitsPerValRec + 1; //$00000 
int counter = 0;
bool counterState = false;
String receivedString; 

void setup() {
  Serial.begin(9600);
  servoThumb.attach(7);
  servoIndex.attach(9);
  servoMiddle.attach(11);
  servoRing.attach(8);
  servoPinky.attach(10);
}

void receiveData(){
  while(Serial.available()){
    char c = Serial.read();
    if (c == '$'){
      counterState = true; 
    }
    if (counterState){
      if (counter < stringLength){
        receivedString = String(receivedString + c);
        counter++;
      }
      if (counter >= stringLength){
        //$00000
        for (int i = 0; i < numOfValsRec; i++){
          valsRec[i] = receivedString.substring(i * digitsPerValRec + 1, i * digitsPerValRec + 2).toInt();
        }
        receivedString = "";
        counter = 0;
        counterState = false;
      }
    }
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  receiveData();
  if (valsRec[0] == 1){
    servoThumb.write(180);
  }
  else {
    servoThumb.write(0);
  }

  if (valsRec[1] == 2){
    servoIndex.write(180);
  }
  else {
    servoIndex.write(0);
  }

  if (valsRec[2] == 3){
    servoMiddle.write(180);
  }
  else {
    servoMiddle.write(0);
  }

  if (valsRec[3] == 4){
    servoRing.write(180);
  }
  else {
    servoRing.write(0);
  }

  if (valsRec[4] == 5){
    servoPinky.write(180);
  }
  else {
    servoPinky.write(0);
  }
}
