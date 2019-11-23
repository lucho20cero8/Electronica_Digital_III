/*****
 Creado por:
    Jhon Mendoza
    Camilo Leon
    Julian Alcala
*****/

// Se cargan las librerias ESP8266WiFi y PubSubClient.
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

//"Recuerda que la red debe ser la misma a la cual esta conectada la Raspberry pi".
// Cambia la red y contraseña a la cual va a estar conectada tu ESP.
const char* ssid = "Nombre Red";
const char* password = "Contraseña Red";

// Cambia la IP de direccion de tu Raspberry, esto conectara a tu Broker MQTT en la Raspberry.
const char* mqtt_server = "IP de tu BROKER";


// Inicializa tu espClient.
WiFiClient espClient;
PubSubClient client(espClient);

// Se inicializa los GPIO de tu ESP8266.
const int buzzerGPIO5 = 5;
// 4 Leds RGB.
const int ledGPIO16 = 16;
const int ledGPIO4 = 4;
const int ledGPIO0 = 0;
const int ledGPIO2 = 2;


// Variables globales para pulsador y switch
//Pulsador== controlar la puerta(Servomotor).
//Pulsador2== controlar el estado del profesor.
char      charPulsador[15];
String    strPulsador;
String    strPulsadorUltimo;

char      charPulsador2[15];
String    strPulsador2;
String    strPulsadorUltimo2;

// Variables de tiempo auxiliar
long now = millis();
long lastMeasure = 0;

//No cambie la siguiente funcion, ya que esta función conecta su ESP8266 a su Red.
void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Conectando a ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("WiFi conectado - Dirección IP del ESP:");
  Serial.println(WiFi.localIP());
}

// Esta función se va a ejecutar al momento en el que un dispositivo publique un mensaje a un Topic al que está suscrito su ESP8266.
// Esta función se puede modificar para que cuando sus dispositivos publiquen un mensaje a un Topic que su ESP este supcrito, este dispositivo haga algo.
void callback(String topic, byte* message, unsigned int length) {
  Serial.print("Mensaje recibido del tema: ");
  Serial.print(topic);
  Serial.print(". Mensaje: ");
  String messageTemp;
  
  for (int i = 0; i < length; i++) {
    Serial.print((char)message[i]);
    messageTemp += (char)message[i];
  }
  Serial.println();
  // Se pueden agregar las condiciones que usted prefiera para controlar más GPIO con MQTT 
  // Si se recibe un mensaje del Topic "profesor1/4", verifica en que estado esta el pulsador, esto activa los GPIO de acuerdo al mensaje y la configuracion que se desee.
  if((topic=="profesor1/4") && (strPulsador2=="Disponible")){
      Serial.print("Alarma de estado: Disponible ");
      if(messageTemp == "1"){
        int i=0;
        while(i<8){
          tone(5,1000, 200);
          digitalWrite(ledGPIO16, HIGH);
          digitalWrite(ledGPIO4, HIGH);
          digitalWrite(ledGPIO0, HIGH);
          digitalWrite(ledGPIO2, HIGH);
          delay(500);
          i+=1;
        }
        digitalWrite(ledGPIO16, LOW);
        digitalWrite(ledGPIO4, LOW);
        digitalWrite(ledGPIO0, LOW);
        digitalWrite(ledGPIO2, LOW);
      }
  }
  if((topic=="profesor1/4") && (strPulsador2=="Ocupado")){
      Serial.print("Alarma de estado: Ocupado ");
      if(messageTemp == "1"){
        int j=0;
        while(j<8){
          tone(5,200, 600);
          digitalWrite(ledGPIO16, HIGH);
          digitalWrite(ledGPIO4, HIGH);
          digitalWrite(ledGPIO0, HIGH);
          digitalWrite(ledGPIO2, HIGH);
        delay(600);
          j+=1;
        }
        digitalWrite(ledGPIO16, LOW);
        digitalWrite(ledGPIO4, LOW);
        digitalWrite(ledGPIO0, LOW);
        digitalWrite(ledGPIO2, LOW);
      }
  }
  Serial.println();
  Serial.println();
}

// Esta función vuelve a conectar su ESP8266 a su BROKER MQTT
// Cambie la función a continuación si desea suscribirse a más temas con su ESP8266
void reconnect() {
  // Bucle hasta que estemos reconectados
  while (!client.connected()) {
    Serial.print(""conectando a MQTT ...");
    if (client.connect("ESPprofesor1")) {
      Serial.println("Conectado");  
      // Usted puede subscribirse a los Topics que quiera, para controlar mas cosas.
      client.subscribe("profesor1/4");
    } else {
      Serial.print("falló, rc=");
      Serial.print(client.state());
      Serial.println(" intentando nuevamente cada 5 segundos");
      delay(5000);
    }
  }
}

// La función de setup establece sus ESP GPIO en Salidas, Entradas e inicia la comunicación en serie a una velocidad en baudios de 115200
// Establece tu BROKER MQTT y establece la función de callback, La función de callback es la que recibe los mensajes y en realidad controla los las Salidas.
void setup() {
//  Salidas
  pinMode(buzzerGPIO5, OUTPUT);
  pinMode(ledGPIO16, OUTPUT);
  pinMode(ledGPIO4, OUTPUT);
  pinMode(ledGPIO0, OUTPUT);
  pinMode(ledGPIO2, OUTPUT);
//  Entradas
  pinMode(14,INPUT_PULLUP);  //D5
  pinMode(12,INPUT_PULLUP);  //
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

// En esta funcion se lee los ESP GPIO de entradas y segun su estado se publica a diferentes TOPICS en el BROKER.
void loop() {
  if (!client.connected()) {
    reconnect();
  }
  if(!client.loop())
    client.connect("ESPprofesor1");
    if(digitalRead(14)== 1){
      strPulsador = "Abierta";
    } else {
      strPulsador = "Cerrada";
    }
    if(digitalRead(12)== 0){
      strPulsador2 = "Ocupado";
    } else {
      strPulsador2 = "Disponible";
    }

    if (strPulsador != strPulsadorUltimo){  //envia el estado del pulsador solamente cuando cambia
      strPulsadorUltimo = strPulsador;
      strPulsador.toCharArray(charPulsador, 15);
      Serial.print("\nEnviando pulsador1 valor: ");
      Serial.print(strPulsador);
      Serial.print("...");
      if(! client.publish("/profesor1/puerta", charPulsador)){
        Serial.print("Falló");
      } else {
        Serial.print("OK");
        Serial.print("\n");
        Serial.print(charPulsador);
      }
      delay(1000);
    }
    if (strPulsador2 != strPulsadorUltimo2){  //envia el estado del pulsador solamente cuando cambia
      strPulsadorUltimo2 = strPulsador2;
      strPulsador2.toCharArray(charPulsador2, 15);
      Serial.print("\nEnviando pulsador2 valor: ");
      Serial.print(strPulsador2);
      Serial.print("...");
      if(! client.publish("/profesor1/estado", charPulsador2)){
        Serial.print("Falló");
      } else {
        Serial.print("OK");
        Serial.print("\n");
        Serial.print(charPulsador2);
      }
      delay(1000);
    }
}
