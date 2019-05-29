#include <NewPing.h>
// ---------------------------------------------------------------------------
// Example NewPing library sketch that pings 3 sensors 20 times a second.
// ---------------------------------------------------------------------------

#define SONAR_NUM 2      // Number of sensors.
#define MAX_DISTANCE 400 // Maximum distance (in cm) to ping.
int distancia_1 = 0;
int distancia_2 = 0;
int distancia1 = 0;
int distancia2 = 0;
int energia = 8;

  NewPing sonar[SONAR_NUM] = {   // Sensor object array.
  NewPing(4, 5, MAX_DISTANCE), // Each sensor's trigger pin, echo pin, and max distance to ping.
  NewPing(6, 7, MAX_DISTANCE)
  };
void setup() {
  Serial.begin(9600); // Open serial monitor at 115200 baud to see ping results.
  pinMode(energia, OUTPUT);
  digitalWrite(energia, HIGH);
}
void loop() {
  
  distancia_1 = sonar[1].ping_cm();
  distancia_2 = sonar[0].ping_cm();
 
  if (distancia_1 < 10 && distancia_1 > 1)
    {
     distancia1 = 1;
    }
  else
  {
    distancia1 = 0;
  }
  if (distancia_2 < 10 && distancia_2 > 1)
    {
     distancia2 = 1;
    }
  else
  {
    distancia2 = 0;
  }
   Serial.print(distancia1);
   Serial.print(":");
   Serial.print(distancia2);
   Serial.print(": ");
   Serial.println();
}
