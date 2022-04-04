#define dirPin1 3
#define stepPin1 2
#define dirPin2 5
#define stepPin2 4
#define dirPin3 9
#define stepPin3 8
#define stepsPerRevolution 200

//float currentAngle = 0;
//float angle = 0;
//float incangle = 0;
float stepPerAngle = 1.8; // full step = 1.8
float tolerance = 1.0;
int pulseWidth = 1000;
int updatesPerLoop = 100;

int firstbracket;
int secondbracket;
int endnr;

float angle1;
float angle2;
float angle3;
float microStepFactor1 = 1.0;
float microStepFactor2 = 2.0;
float microStepFactor3 = 2.0;
//int numstep1;
//int numstep2;
//int numstep3;
//float n1;
//float n2;
//float n3;
float stepAngle1;
float stepAngle2;
float stepAngle3;
float currentAngle1;
float currentAngle2;
float currentAngle3;
String angle1st;
String angle2st;
String angle3st;
String firststring;
String secondstring;
String thirdstring;

// Debug iterations in update
//int counter = 0;

void setup() {
  Serial.begin(9600);
  // Sets the two pins as Outputs
  pinMode(stepPin1, OUTPUT);
  pinMode(dirPin1, OUTPUT);
  pinMode(stepPin2, OUTPUT);
  pinMode(dirPin2, OUTPUT);
  pinMode(stepPin3, OUTPUT);
  pinMode(dirPin3, OUTPUT);
  digitalWrite(dirPin1, HIGH);
  digitalWrite(dirPin2, HIGH);
  digitalWrite(dirPin3, HIGH);

}

void loop() {
  TryReadSerial();
  DebugAngles();
  for (int i = 0; i < updatesPerLoop; i++)
    UpdateMotors();
}
void TryReadSerial() {
  if (Serial.available() > 0) {
    String strdata = Serial.readStringUntil('\n');

    firstbracket = strdata.indexOf(";");
    secondbracket = strdata.indexOf(";", (firstbracket + 1));
    endnr = strdata.length();

    angle1st = strdata.substring(0, firstbracket);
    angle2st = strdata.substring((firstbracket + 1), secondbracket);
    angle3st = strdata.substring((secondbracket + 1), endnr);

    angle1 = angle1st.toFloat();
    angle2 = angle2st.toFloat();
    angle3 = angle3st.toFloat();
    //Serial.println("Angles Received");
  } else {
    //Serial.println("Angles Not Received");
  }
}
void DebugAngles() {
  //Serial.print("Angle1 ");
  Serial.print(angle1);
  Serial.print(",");
  //Serial.print("currentAngle1 ");
  Serial.print(currentAngle1);
  Serial.print(",");
  //Serial.print("Angle2 ");
  Serial.print(angle2);
  Serial.print(",");
  //Serial.print("currentAngle2 ");
  Serial.print(currentAngle2);
  Serial.print(",");
  //Serial.print("Angle3 ");
  Serial.print(angle3);
  Serial.print(",");
  //Serial.print("currentAngle3 ");
  Serial.println(currentAngle3);
}
void UpdateMotors() {
  stepAngle1 = 0;
  stepAngle2 = 0;
  stepAngle3 = 0;
  if (abs(currentAngle1 - angle1) > tolerance) {
    //    float n1;
    //    int numstep1;
    if (currentAngle1 < angle1) {
      digitalWrite(dirPin1, HIGH);
      //      n1 = angle1 - currentAngle1;
      //      numstep1 = n1 / stepPerAngle;
      stepAngle1 = stepPerAngle / microStepFactor1;
    }

    else if (currentAngle1 > angle1) {
      digitalWrite(dirPin1, LOW);
      //      n1 = currentAngle1 - angle1;
      //      if ( angle1 == 0) {
      //        n1 = currentAngle1;
      //      }
      //      numstep1 = round(n1 / stepPerAngle);
      stepAngle1 = -stepPerAngle / microStepFactor1;
    }

    //    for (int x = 0; x < numstep1; x++) {
    //        digitalWrite(stepPin1, HIGH);
    //        delayMicroseconds(pulseWidth);
    //        digitalWrite(stepPin1, LOW);
    //        delayMicroseconds(pulseWidth);
    //    }
    //    currentAngle1 = angle1;
    currentAngle1 += stepAngle1;
  }
  if (abs(currentAngle2 - angle2) > tolerance) {

    if (currentAngle2 < angle2) {
      digitalWrite(dirPin2, HIGH);
      //n2 = angle2 - currentAngle2;
      //numstep2 = n2 / stepPerAngle;
      stepAngle2 = stepPerAngle / microStepFactor2;
    }

    else if (currentAngle2 > angle2) {
      digitalWrite(dirPin2, LOW);
      //n2 = currentAngle2 - angle2;
      //if ( angle2 == 0) {
      //  n2 = currentAngle2;
      //}
      //numstep2 = n2 / stepPerAngle;
      stepAngle2 = -stepPerAngle / microStepFactor2;
    }

    //for (int x = 0; x < numstep2; x++) {
    //    digitalWrite(stepPin2, HIGH);
    //    delayMicroseconds(pulseWidth);
    
    //    digitalWrite(stepPin2, LOW);
    //    delayMicroseconds(pulseWidth);
    //}
    //currentAngle2 = angle2;
    currentAngle2 += stepAngle2;
  }
  if (abs(currentAngle3 - angle3) > tolerance) {

    if (currentAngle3 < angle3) {
      digitalWrite(dirPin3, HIGH);
      //n3 = angle3 - currentAngle3;
      //numstep3 = n3 / stepPerAngle;
      stepAngle3 = stepPerAngle / microStepFactor3;
    }

    else if (currentAngle3 > angle3) {
      digitalWrite(dirPin3, LOW);
      //n3 = currentAngle3 - angle3;
      //if ( angle3 == 0) {
      //  n3 = currentAngle3;
      //}
      //numstep3 = n3 / stepPerAngle;
      stepAngle3 = -stepPerAngle / microStepFactor3;
    }

    //for (int x = 0; x < numstep3; x++) {
    //    digitalWrite(stepPin3, HIGH);
    //    delayMicroseconds(pulseWidth);
    //    digitalWrite(stepPin3, LOW);
    //    delayMicroseconds(pulseWidth);
    
    //}
    //currentAngle3 = angle3;
    currentAngle3 += stepAngle3;
  }

  if (stepAngle1 != 0)
    digitalWrite(stepPin1, HIGH);
  if (stepAngle2 != 0)
    digitalWrite(stepPin2, HIGH);
  if (stepAngle3 != 0)
    digitalWrite(stepPin3, HIGH);
  if ((stepAngle1 != 0) || (stepAngle2 != 0) || (stepAngle3 != 0)){
    //counter +=1;
    delayMicroseconds(pulseWidth);
  }else {
    // Debug iterations in update
    //if (counter != 0){
    //  Serial.println();
    //  Serial.println(counter);
    //  Serial.println();
    //  counter = 0;
    //}
  }

  if (stepAngle1 != 0)
    digitalWrite(stepPin1, LOW);
  if (stepAngle2 != 0)
    digitalWrite(stepPin2, LOW);
  if (stepAngle3 != 0)
    digitalWrite(stepPin3, LOW);
  if ((stepAngle1 != 0) || (stepAngle2 != 0) || (stepAngle3 != 0)){
    delayMicroseconds(pulseWidth);
  }
  //delay(1);
}
