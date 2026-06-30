// C++ code revised
// Range 10 - 334 distance

int rangeNum = 334;
const int trigPin = 9;  
const int echoPin = 10;
const int greenPin1 = 13;
const int greenPin2 = 12;
const int greenPin3 = 11;
const int greenPin4 = 8;
const int greenPin5 = 7;
const int yellowPin1 = 6;
const int yellowPin2 = 5;
const int orangePin1 = 4;
const int redPin1 = 3;
const int redPin2 = 2;

float duration, distance;  

long randNum1;
long randNum2;


void setup() {  
  	
  	randomSeed(analogRead(0));
  
  	pinMode(greenPin1, OUTPUT);
  	pinMode(greenPin2, OUTPUT);
  	pinMode(greenPin3, OUTPUT);
  	pinMode(greenPin4, OUTPUT);
  	pinMode(greenPin5, OUTPUT);
  	pinMode(yellowPin1, OUTPUT);
  	pinMode(yellowPin2, OUTPUT);
  	pinMode(orangePin1, OUTPUT);
  	pinMode(redPin1, OUTPUT);
  	pinMode(redPin2, OUTPUT);
  
    pinMode(trigPin, OUTPUT);  
    pinMode(echoPin, INPUT);  
    Serial.begin(9600);  
} 

void loop() {  
    digitalWrite(trigPin, LOW);  
    delayMicroseconds(2);  
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
      
    duration = pulseIn(echoPin, HIGH);    	
    distance = (duration*.0343)/2;  
    Serial.print("Distance: ");
    Serial.println(distance);
    delay(100);
    
    digitalWrite(greenPin1, HIGH); // Use the name to control the hardware
    delay(100);
    
    randNum1 = random(80, 150);
    randNum2 = random(10, 30);
    
    if (distance < (0.9 * rangeNum) && distance > (0.8 * rangeNum) ){
        digitalWrite(greenPin2, HIGH);
        delay(randNum1);
        digitalWrite(greenPin2, LOW);
        delay(randNum2);
    }else if (distance < (0.8 * rangeNum)){
        digitalWrite(greenPin2, HIGH);
    }else {
        digitalWrite(greenPin2, LOW);
    }

    if (distance < (0.8 * rangeNum) && distance > (0.7 * rangeNum) ){
        digitalWrite(greenPin3, HIGH);
        delay(randNum1);
        digitalWrite(greenPin3, LOW);
        delay(randNum2);
    }else if (distance < (0.7 * rangeNum)){
        digitalWrite(greenPin3, HIGH);
    }else {
        digitalWrite(greenPin3, LOW);
    }

    if (distance < (0.7 * rangeNum) && distance > (0.6 * rangeNum) ){
        digitalWrite(greenPin4, HIGH);
        delay(randNum1);
        digitalWrite(greenPin4, LOW);
        delay(randNum2);
      
    }else if (distance < (0.6 * rangeNum)){
        digitalWrite(greenPin4, HIGH);
    }else {
        digitalWrite(greenPin4, LOW);
    }
    
    if (distance < (0.6 * rangeNum) && distance > (0.5 * rangeNum) ){
        digitalWrite(greenPin5, HIGH);
        delay(randNum1);
        digitalWrite(greenPin5, LOW);
        delay(randNum2);
      
    }else if (distance < (0.5 * rangeNum)){
        digitalWrite(greenPin5, HIGH);
    }else {
        digitalWrite(greenPin5, LOW);
    }

    if (distance < (0.5 * rangeNum) && distance > (0.4 * rangeNum) ){
        digitalWrite(yellowPin1, HIGH);
        delay(randNum1);
        digitalWrite(yellowPin1, LOW);
        delay(randNum2);
      
    }else if (distance < (0.4 * rangeNum)){
        digitalWrite(yellowPin1, HIGH);
    }else {
        digitalWrite(yellowPin1, LOW);
    }

    if (distance < (0.4 * rangeNum) && distance > (0.3 * rangeNum) ){
        digitalWrite(yellowPin2, HIGH);
        delay(randNum1);
        digitalWrite(yellowPin2, LOW);
        delay(randNum2);
      
    }else if (distance < (0.3 * rangeNum)){
        digitalWrite(yellowPin2, HIGH);
    }else {
        digitalWrite(yellowPin2, LOW);
    }

    if (distance < (0.3 * rangeNum) && distance > (0.2 * rangeNum) ){
        digitalWrite(orangePin1, HIGH);
        delay(randNum1);
        digitalWrite(orangePin1, LOW);
        delay(randNum2);
      
    }else if (distance < (0.2 * rangeNum)){
        digitalWrite(orangePin1, HIGH);
    }else {
        digitalWrite(orangePin1, LOW);
    }

    if (distance < (0.2 * rangeNum) && distance > (0.1 * rangeNum) ){
        digitalWrite(redPin1, HIGH);
        delay(randNum1);
        digitalWrite(redPin1, LOW);
        delay(randNum2);
      
    }else if (distance < (0.1 * rangeNum)){
        digitalWrite(redPin1, HIGH);
    }else {
        digitalWrite(redPin1, LOW);
    }

    if (distance < (0.1 * rangeNum) && distance >= (0 * rangeNum) ){
        digitalWrite(redPin2, HIGH);
        delay(randNum1);
        digitalWrite(redPin2, LOW);
        delay(randNum2);
    }else {
        digitalWrite(redPin2, LOW);
    }
        
  
}