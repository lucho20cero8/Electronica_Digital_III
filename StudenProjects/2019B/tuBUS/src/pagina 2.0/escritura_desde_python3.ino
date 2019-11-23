#include <SPI.h>
#include <MFRC522.h>
constexpr uint8_t RST_PIN = 9;     // Configurable, see typical pin layout above
constexpr uint8_t SS_PIN = 10;     // Configurable, see typical pin layout above
const int inputPin = 2;
const int inputpin = 3;
const int ledPIN = 4;
const int ledpIN = 5;
int actualizar = 0;
int recargar = 0;
MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance
char c;
char p = 1;
int leer;
int bandera = 1;
void setup() {
  Serial.begin(9600);        // Initialize serial communications with the PC
  pinMode(inputPin, INPUT);
  pinMode(inputpin, INPUT);
  pinMode(ledPIN , OUTPUT);
  pinMode(ledpIN , OUTPUT);
  SPI.begin();               // Init SPI bus
  mfrc522.PCD_Init();        // Init MFRC522 card
}
void loop()
{
  actualizar = digitalRead(inputpin);
  recargar = digitalRead(inputPin);
  if (actualizar == LOW) {
    digitalWrite(ledPIN , HIGH);
    Leer();
  }
  if (recargar == LOW) {
    digitalWrite(ledpIN , HIGH);
    Escribir();
  }
  digitalWrite(ledPIN , LOW);
  digitalWrite(ledpIN , LOW);


}
void Escribir()
{
  // Prepare key - all keys are set to FFFFFFFFFFFFh at chip delivery from the factory.
  MFRC522::MIFARE_Key key;
  byte buffer[34];
  byte block;
  MFRC522::StatusCode status;
  byte len;
  Serial.setTimeout(20000L) ;     // wait until 20 seconds for input from serial
  // Ask personal data: Family name
  //Serial.println(F("Entra codigo terminando con #"));
  len = Serial.readBytesUntil('#', (char *) buffer, 30) ;
  for (byte i = len; i < 30; i++) buffer[i] = ' ';     // pad with spaces
  for (byte i = 0; i < 6; i++) key.keyByte[i] = 0xFF;
  // Look for new cards
  while ( ! mfrc522.PICC_IsNewCardPresent()) {
    //return;
  }

  // Select one of the cards
  while ( ! mfrc522.PICC_ReadCardSerial()) {
    //return;
  }

  //Serial.print(F("Card UID:"));    //Dump UID
  for (byte i = 0; i < mfrc522.uid.size; i++) {
    //Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
    //Serial.print(mfrc522.uid.uidByte[i], HEX);
  }
  //Serial.print(F(" PICC type: "));   // Dump PICC type
  MFRC522::PICC_Type piccType = mfrc522.PICC_GetType(mfrc522.uid.sak);
  //Serial.println(mfrc522.PICC_GetTypeName(piccType));

  block = 1;
  //Serial.println(F("Authenticating using key A..."));
  status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, block, &key, &(mfrc522.uid));
  if (status != MFRC522::STATUS_OK) {
    //Serial.print(F("PCD_Authenticate() failed: "));
    //Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }
  //else Serial.println(F("PCD_Authenticate() success: "));

  // Write block
  status = mfrc522.MIFARE_Write(block, buffer, 16);
  if (status != MFRC522::STATUS_OK) {
    //  Serial.print(F("MIFARE_Write() failed: "));
    //Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }
  //else Serial.println(F("MIFARE_Write() success: "));
  //Serial.println("Escrito correctamente");
  mfrc522.PICC_HaltA(); // Halt PICC
  mfrc522.PCD_StopCrypto1();  // Stop encryption on PCD
}
void Leer()
{
  MFRC522::MIFARE_Key key;
  for (byte i = 0; i < 6; i++) key.keyByte[i] = 0xFF;
  byte block;
  byte len;
  MFRC522::StatusCode status;
  while ( ! mfrc522.PICC_IsNewCardPresent()) {
    //return;
  }
  while ( ! mfrc522.PICC_ReadCardSerial()) {
    //return;
  }

  //mfrc522.PICC_DumpDetailsToSerial(&(mfrc522.uid)); //dump some details about the card

  len = 18;
  byte buffer2[18];
  block = 1;

  status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, 1, &key, &(mfrc522.uid)); //line 834
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("Authentication failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }

  status = mfrc522.MIFARE_Read(block, buffer2, &len);
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("Reading failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }
  //PRINT LAST NAME
  String leer = "";
  for (uint8_t i = 0; i < 6; i++) {
    leer += (char)buffer2[i];
  }
  //saldo = leer-1800;
  Serial.println(leer);
  //  Serial.println(saldo);
  //----------------------------------------

  delay(1000); //change value if you want to read cards faster

  mfrc522.PICC_HaltA();
  mfrc522.PCD_StopCrypto1();


}
