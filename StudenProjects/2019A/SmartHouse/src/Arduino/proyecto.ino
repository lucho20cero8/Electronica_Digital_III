#include <DallasTemperature.h>
#include <OneWire.h>
#include <SPI.h>      // incluye libreria bus SPI
#include <MFRC522.h>      // incluye libreria especifica para MFRC522
#include <Servo.h>
Servo servo;

//sensor temperatura
#define temperatura 5                        //Se declara el pin donde se conectará la DATA
OneWire ourWire(temperatura);                //Se establece el pin declarado como bus para la comunicación OneWire
DallasTemperature sensors(&ourWire);
//nfc
#define RST_PIN  9      // constante para referenciar pin de reset
#define SS_PIN  10      // constante para referenciar pin de slave select

MFRC522 mfrc522(SS_PIN, RST_PIN); // crea objeto mfrc522 enviando pines de slave select y reset

byte LecturaUID[4];         // crea array para almacenar el UID leido
byte Usuario1[4]= {0x61, 0xC5, 0xE3, 0x73} ;    // UID de tarjeta leido en programa 1
byte Usuario2[4]= {0xB6, 0xD5, 0xE6, 0x1F} ;    // UID de llavero leido en programa 1
//servo
const int pinservo = 8; //conectar servo pin digital 8
const int pulsominimo = 1000; //pulso para 0°
const int pulsomaximo = 2000; //pulso para 180°
//pines
const int flama1 = 2;
const int flama2 = 3;
const int flama3 = 4;
const int buzzer = 6;
const int LDR0 = A0;
const int LDR1 = A1;
const int LDR2 = A2;
const int LDR3 = A3;
const int LDR4 = A4;
const int LDR5 = A5;
//variables
int valorflama1;
int valorflama2;
int valorflama3;
int valorLDR0 = 0;
int valorLDR1 = 0;
int valorLDR2 = 0;
int valorLDR3 = 0;
int valorLDR4 = 0;
int valorLDR5 = 0;
int contador1 = 0;
int contador2 = 0;
int contador3 = 0;

void setup() {
    Serial.begin(9600);
    servo.attach(pinservo, pulsominimo, pulsomaximo); //(pin donde esta conectado el servo, pulso minimo, pulso maximo) 
    //sensores
    pinMode(flama1, INPUT);
    pinMode(flama2, INPUT);
    pinMode(flama3, INPUT);
    pinMode(buzzer, OUTPUT);
    SPI.begin();        // inicializa bus SPI
    mfrc522.PCD_Init();     // inicializa modulo lector
    sensors.begin(); 
    Serial.println("Listo");
}

void loop() {
  sensors.requestTemperatures();
  valorflama1 = digitalRead(flama1);
  valorflama2 = digitalRead(flama2);
  valorflama3 = digitalRead(flama3);
  valorLDR0 = analogRead(LDR0);
  valorLDR1 = analogRead(LDR1);
  valorLDR2 = analogRead(LDR2);
  valorLDR3 = analogRead(LDR3);
  valorLDR4 = analogRead(LDR4);
  valorLDR5 = analogRead(LDR5);
  //buzzer
  if(valorflama1 == 0 || valorflama2 == 0 || valorflama3 == 0)
  {
    digitalWrite(buzzer, HIGH);
  }
  else
  {
    digitalWrite(buzzer, LOW);
  }
  //fotoresistencias
  if(valorLDR0<600 && valorLDR1>600)
  {
    contador1++;
  }
  else if(valorLDR1<600 && valorLDR0>600 && contador1>0)
  {
    contador1--;
  }
  else if(valorLDR2<600 && valorLDR3>600)
  {
    contador2++;
  }
  else if(valorLDR3<600 && valorLDR2>600 && contador2>0)
  {
    contador2--;
  }


  Serial.print("flama1:");
  Serial.print(valorflama1);
  Serial.print(":flama2:");
  Serial.print(valorflama2);
  Serial.print(":flama3:");
  Serial.print(valorflama3);
  Serial.print(":temperatura:");
  Serial.print(sensors.getTempCByIndex(0)); //valor sensor temperatura
  Serial.print(":contador1:");
  Serial.print(contador1);
  Serial.print(":contador2:");
  Serial.print(contador2);
  //Serial.print(":contador3:");
  //Serial.print(contador3);
  /*Serial.print(":LDR0:");
  Serial.print(valorLDR0);
  Serial.print(":LDR1:");
  Serial.print(valorLDR1);
  Serial.print(":LDR2:");
  Serial.print(valorLDR2);
  Serial.print(":LDR3:");
  Serial.print(valorLDR3);*/
  Serial.print(":");
  

  if ( ! mfrc522.PICC_IsNewCardPresent())
  { // si no hay una tarjeta presente
    Serial.print("esperandoTarjeta");
    servo.write(0);
    Serial.println();
    return;           // retorna al loop esperando por una tarjeta
  }
  if ( ! mfrc522.PICC_ReadCardSerial())
  {     // si no puede obtener datos de la tarjeta
    Serial.print("esperandoTarjeta");
    servo.write(0);
    Serial.println();
    return;           // retorna al loop esperando por otra tarjeta
  } 
    for (byte i = 0; i < mfrc522.uid.size; i++) 
    { // bucle recorre de a un byte por vez el UID
      LecturaUID[i]=mfrc522.uid.uidByte[i];     // almacena en array el byte del UID leido      
    }                     
                    
          if(comparaUID(LecturaUID, Usuario1))
          { // llama a funcion comparaUID con Usuario1
            Serial.print("Bienvenido"); // si retorna verdadero muestra texto bienvenida
            servo.write(180);
            delay(5000);
          }
          else if(comparaUID(LecturaUID, Usuario2))
          { // llama a funcion comparaUID con Usuario2
            Serial.print("Bienvenido"); // si retorna verdadero muestra texto bienvenida
            servo.write(180);
            delay(5000);
          }
          else
          {           // si retorna falso
            Serial.print("noAutorizado");    // muestra texto equivalente a acceso denegado      
            servo.write(0);
          }
         
  Serial.println();
  mfrc522.PICC_HaltA();     // detiene comunicacion con tarjeta  
  }

  boolean comparaUID(byte lectura[],byte usuario[]) // funcion comparaUID
{
  for (byte i=0; i < mfrc522.uid.size; i++)
  {    // bucle recorre de a un byte por vez el UID
  if(lectura[i] != usuario[i])
  {// si byte de UID leido es distinto a usuario
    return(false);          // retorna falso
  }
  }
  return(true);           // si los 4 bytes coinciden retorna verdadero
}
