#define SENSOR_A 2
#define SENSOR_B 3
#define SENSOR_C 4
#define SENSOR_D 5
const int ledPIN = 9;
unsigned long duracion = 0;
void setup() {
  Serial.begin(9600);  
      pinMode(SENSOR_A, INPUT_PULLUP);
      pinMode(SENSOR_B, INPUT_PULLUP);
      pinMode(SENSOR_C, INPUT_PULLUP);
      pinMode(SENSOR_D, INPUT_PULLUP);
      pinMode(ledPIN , OUTPUT);
 }
void loop() {
  int s1 = detectaFlanco(SENSOR_A);
  int s2 = detectaFlanco(SENSOR_B); 
  int s3 = detectaFlanco1(SENSOR_C);
  int s4 = detectaFlanco1(SENSOR_D);     
  if (s1==0 && s2==-1){    
      Serial.println(1);     
  }   
  if (s2==0 && s1==-1){
      Serial.println(2);   
  } 
   
  if (s3==0 && s4==-1){    
      Serial.println(3);      
  }
  if (s4==0 && s3==-1){    
      Serial.println(4);
      digitalWrite(ledPIN , HIGH);   // poner el Pin en HIGH
      delay(2000);                   // esperar un segundo
      digitalWrite(ledPIN , LOW);    // poner el Pin en LOW
   }
 
  else {
   Serial.println(0); 
   delay(50);
  }
 }
boolean detectaFlancoAscendente(int pin) {
  static boolean anterior_estado = digitalRead(pin);
  boolean estado = digitalRead(pin);

  if ((anterior_estado != estado) && (estado == HIGH)) {
    anterior_estado = estado; 
    return true;
  }
  else {
    anterior_estado = estado;
    return false;
  }
}

boolean detectaFlancoDescendente(int pin) {
  static boolean anterior_estado = digitalRead(pin);
  boolean estado = digitalRead(pin);

  if ((anterior_estado != estado) && (estado == LOW)) {
    anterior_estado = estado;
    return 1;
  }
  else {
    anterior_estado = estado;
    return 0;
  }}

int detectaFlanco(int pin) {
  //Devuelve 1 flanco ascendente, -1 flanco descendente y 0 si no hay nada
  static boolean anterior_estado = digitalRead(pin);
  boolean estado = digitalRead(pin);

  if (anterior_estado != estado) {
    if (estado == HIGH) {
      anterior_estado = estado;
      return 1;
    }
    else {
      anterior_estado = estado;
      return -1;
    }
  }
  else {
    return 0;
  }
}
  int detectaFlanco1(int pin) {
  //Devuelve 1 flanco ascendente, -1 flanco descendente y 0 si no hay nada
  static boolean anterior_estado = digitalRead(pin);
  boolean estado = digitalRead(pin);

  if (anterior_estado != estado) {
    if (estado == HIGH) {
      anterior_estado = estado;
      return 1;
    }
    else {
      anterior_estado = estado;
      return -1;
    }
  }
  else {
    return 0;
  }
}
