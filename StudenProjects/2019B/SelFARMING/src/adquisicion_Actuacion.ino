#include <Wire.h>
#include <BH1750.h>

BH1750 luxometro;
int nmpin = 13; // Sensor de nivel medio
int nbpin = 12; // Sensor de nivel bajo
int hapin = A2; // Sensor de humedad
int IN1 = 8;  // Pin digital 8 de Arduino a IN1 de modulo controlador
int IN2 = 9;  // Pin digital 9 de Arduino a IN2 de modulo controlador
int IN3 = 10; // Pin digital 10 de Arduino a IN3 de modulo controlador
int IN4 = 11; // Pin digital 11 de Arduino a IN4 de modulo controlador
int demora = 10;  // Demora entre pasos, no debe ser menor a 10 ms
int mssg = 0; // Variable para guardar el mensaje

void setup()
{
  Serial.begin(9600);
  Wire.begin();
  luxometro.begin();
  pinMode(nmpin,INPUT);
  pinMode(nbpin,INPUT);
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
  pinMode(IN3,OUTPUT);
  pinMode(IN4,OUTPUT);
}

void motor()
{
  if (Serial.available() > 0)
  {
    mssg = Serial.read(); // Leemos el serial
    if(mssg == '1')
    {
      for (int i = 0; i < 1536; i++)  // 512*4 = 2048 pasos
      {
        digitalWrite(IN1,HIGH);  // Paso 1
        digitalWrite(IN2,HIGH);
        digitalWrite(IN3,LOW);
        digitalWrite(IN4,LOW);
        delay(demora);
        digitalWrite(IN1,LOW); // Paso 2
        digitalWrite(IN2,HIGH);
        digitalWrite(IN3,HIGH);
        digitalWrite(IN4,LOW);
        delay(demora);
        digitalWrite(IN1,LOW); // Paso 3
        digitalWrite(IN2,LOW);
        digitalWrite(IN3,HIGH);
        digitalWrite(IN4,HIGH);
        delay(demora);
        digitalWrite(IN1,HIGH);  // Paso 4
        digitalWrite(IN2,LOW);
        digitalWrite(IN3,LOW);
        digitalWrite(IN4,HIGH);
        delay(demora);
      }
    }
    else if(mssg == '0')
    {
      for (int i = 0; i < 1536; i++) // 512*4 = 2048 pasos
      {
        digitalWrite(IN1,LOW); // Paso 1
        digitalWrite(IN2,LOW);
        digitalWrite(IN3,LOW);
        digitalWrite(IN4,HIGH);
        delay(demora);
        digitalWrite(IN1,LOW); // Paso 2
        digitalWrite(IN2,LOW);
        digitalWrite(IN3,HIGH);
        digitalWrite(IN4,LOW);
        delay(demora);
        digitalWrite(IN1,LOW); // Paso 3
        digitalWrite(IN2,HIGH);
        digitalWrite(IN3,LOW);
        digitalWrite(IN4,LOW);
        delay(demora);
        digitalWrite(IN1,HIGH);  // Paso 4
        digitalWrite(IN2,LOW);
        digitalWrite(IN3,LOW);
        digitalWrite(IN4,LOW);
        delay(demora);
      }
    }
  }
}

void loop()
{
  unsigned int iluz = luxometro.readLightLevel();
  int nmedio = digitalRead(nmpin);
  int nbajo = digitalRead(nbpin);
  int humedad = analogRead(hapin);
  float phumedad = 1023.0-humedad;
  phumedad = phumedad*(100.0/1023.0);
  Serial.print(iluz);
  Serial.print(",");
  Serial.print(phumedad);
  Serial.print(",");
  Serial.print(nbajo);
  Serial.println(nmedio);
  motor();
  delay(15000);
}
