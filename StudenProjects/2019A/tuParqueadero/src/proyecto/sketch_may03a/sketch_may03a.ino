#include <NewPing.h>
#include <Multiplexer.h>
#include <LineFollow.h>
#include <ArduinoRobotMotorBoard.h>
#include <EasyTransfer2.h>

// ---------------------------------------------------------------------------
// Example NewPing library sketch that pings 3 sensors 20 times a second.
// ---------------------------------------------------------------------------

#define SONAR_NUM 2      // Number of sensors.
#define MAX_DISTANCE 400 // Maximum distance (in cm) to ping.
int contador = 0;
int distancia_1 = 0;
int distancia_2 = 0;
int distancia1 = 0;
int distancia2 = 0;

NewPing sonar[SONAR_NUM] = {   // Sensor object array.
  NewPing(4, 5, MAX_DISTANCE), // Each sensor's trigger pin, echo pin, and max distance to ping.
  NewPing(6, 7, MAX_DISTANCE)
  };
void setup() {
  Serial.begin(9600); // Open serial monitor at 115200 baud to see ping results.
}
void loop() {
  for (uint8_t i = 0; i < SONAR_NUM; i++) { // Loop through each sensor and display results.
    delay(50); // Wait 50ms between pings (about 20 pings/sec). 29ms should be the shortest delay between pings.
    Serial.print(i);
    Serial.print("=");
    Serial.print(sonar[i].ping_cm());
    Serial.print("cm ");
  }
  distancia_1 = sonar[1].ping_cm();
  distancia_2 = sonar[0].ping_cm();
 
  if (distancia_1 < 100 && distancia_1 > 1)
    {
     distancia1 = 1;
    }
  if (distancia_2 < 100 && distancia_2 > 1)
    {
     distancia2 = 1;
    }
   Serial.print(distancia1);
   Serial.print(",");
   Serial.print(distancia2);
   Serial.println();
}
