#include <SimpleDHT.h>

int actuatorPin = 9;
int sensorPin = A0; // change to A0 if light sensor, 11 is if using DHT11
bool isTemp = true; // true = temp, false = humidity
SimpleDHT11 sensor;

// ranges
int lightRange[] = {0,1023};
int tempRange[] = {0, 50};
int humidityRange[] = {20, 80};

// variables for time and threshold
int threshold = 500; // dependent on sensor selected, set light to 500, humidity 50, temperature 30
long currentMillis = 0;
long previousMillis = 0;

void setup() 
{
  Serial.begin(9600);
  pinMode(actuatorPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  currentMillis = millis();
  delay(50);
  if (currentMillis > previousMillis + 10000) // checking if the last sensor update was 10 seconds ago
  {
    previousMillis = currentMillis;
    sensorRead();
  }
  
  
  if (Serial.available()>0)
  {
    String newString = Serial.readString();    
    int readInt = newString.toInt();
    thresholdSet(readInt);
  }
}

void sensorRead()
{
  if (sensorPin == 11) // temp and humidity
  {
    byte t=0;                                 // variables for temperature and humidity
    byte h=0;
    if(sensor.read(sensorPin,&t,&h,NULL)==0) // read the sensors
    {
      if (isTemp) // temp
      {
        Serial.println((int)t);
        if ((int)t > threshold)
        {
          digitalWrite(actuatorPin, HIGH);
        }
        else
        {
          digitalWrite(actuatorPin, LOW);
        }
      }
      else // humidity
      {
        Serial.println((int)h);
        if ((int)h < threshold)
        {
          digitalWrite(actuatorPin, HIGH);
        }
        else
        {
          digitalWrite(actuatorPin, LOW);
        }
      }
    }
  }
  else // light
  {
    int lightValue = analogRead(A0);
    Serial.println(lightValue);
    if (lightValue < threshold)
    {
      
      digitalWrite(actuatorPin, HIGH);
    }
    else
    {
      digitalWrite(actuatorPin, LOW);
    }

  }
}

void thresholdSet(int readData)
{
  if (sensorPin == 11) // if temp and humidity
  {
    if (isTemp) // temp 
    {
      if (readData >= tempRange[0] && readData <= tempRange[1])
      {
        threshold = readData;
      }
    }
    else // humidity
    {
      if (readData >= humidityRange[0] && readData <= humidityRange[1])
      {
        threshold = readData;
      }
    }
  }
  else // light
  {
    if (readData >= lightRange[0] && readData <= lightRange[1])
    {
      threshold = readData;
    }
  }
}