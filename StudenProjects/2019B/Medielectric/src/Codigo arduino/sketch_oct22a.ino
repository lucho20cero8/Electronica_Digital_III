double A=0;
double C=0;
double B=0;
double D=0;
String voltaje, corriente,fimetro;
double tic,toc,delta,angulo;
int pin=8;
int value=0;
float f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,delta1;

void setup()
{
   Serial.begin(9600);
   pinMode(pin,INPUT);
}
 
void loop() 
{  
   value=digitalRead(pin);
   A= analogRead(A0);   // realizar la lectura
   C= analogRead(A1);   // realizar la lectura                      
   B= (A*(5.00))/1023.00;
   D= (C*(5.00))/1023.00;
   voltaje=String(D);
   corriente=String(B);
   tic= millis();
   if(value==HIGH)
   { //Serial.println("Encendido");
     toc=millis();
     }
   delta=toc-tic;
   angulo=(delta*(360*60))/1000;
   fimetro=String(angulo);

   Serial.println(corriente+":"+voltaje+":"+fimetro);
   delay(33.34);
}
