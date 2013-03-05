#define clockpin 13 // CI
#define enablepin 10 // EI
#define latchpin 9 // LI
#define datapin 11 // DI
 
#define NumLEDs 16
 
int LEDChannels[NumLEDs][3] = {0};
int SB_CommandMode;
int SB_RedCommand;
int SB_GreenCommand;
int SB_BlueCommand;
 
void setup() {
 
   pinMode(datapin, OUTPUT);
   pinMode(latchpin, OUTPUT);
   pinMode(enablepin, OUTPUT);
   pinMode(clockpin, OUTPUT);
   SPCR = (1<<SPE)|(1<<MSTR)|(0<<SPR1)|(0<<SPR0);
   digitalWrite(latchpin, LOW);
   digitalWrite(enablepin, LOW);
 
   Serial.begin(115200);
   for (int i = 1; i < 8; i++)
    {
      setLED(i, 1023, 1023, 1023);
    }
    WriteLEDArray();
}
 
void SB_SendPacket() {
 
    if (SB_CommandMode == B01) {
     SB_RedCommand = 120;
     SB_GreenCommand = 100;
     SB_BlueCommand = 100;
    }
 
    SPDR = SB_CommandMode << 6 | SB_BlueCommand>>4;
    while(!(SPSR & (1<<SPIF)));
    SPDR = SB_BlueCommand<<4 | SB_RedCommand>>6;
    while(!(SPSR & (1<<SPIF)));
    SPDR = SB_RedCommand << 2 | SB_GreenCommand>>8;
    while(!(SPSR & (1<<SPIF)));
    SPDR = SB_GreenCommand;
    while(!(SPSR & (1<<SPIF)));
 
}
 
void WriteLEDArray() {
 
    SB_CommandMode = B00; // Write to PWM control registers
    for (int h = 0;h<NumLEDs;h++) {
	  SB_RedCommand = LEDChannels[h][0];
	  SB_GreenCommand = LEDChannels[h][1];
	  SB_BlueCommand = LEDChannels[h][2];
	  SB_SendPacket();
    }
 
    delayMicroseconds(15);
    digitalWrite(latchpin,HIGH); // latch data into registers
    delayMicroseconds(15);
    digitalWrite(latchpin,LOW);
 
    SB_CommandMode = B01; // Write to current control registers
    for (int z = 0; z < NumLEDs; z++) SB_SendPacket();
    delayMicroseconds(15);
    digitalWrite(latchpin,HIGH); // latch data into registers
    delayMicroseconds(15);
    digitalWrite(latchpin,LOW);
 
}

void setLED(byte LED, int red, int green, int blue)
{
  LEDChannels[LED][0] = red;
  LEDChannels[LED][1] = green;
  LEDChannels[LED][2] = blue;

}

void clearLEDs() {
   for (int i = 1; i < 8; i++)
  {
    setLED(i, 0, 0, 0);
  }
  WriteLEDArray();
}
 
byte inByte;
int in[4] = {0,0,0,0}; 
int pos = 0;
void loop() {

   if (Serial.available() > 0) {

    inByte = Serial.read();
    if ((inByte >= 48) && (inByte <= 57)) { // if ASCII numeric '0' - '9'
      in[pos] = in[pos] * 10 + (inByte - 48);
    }
    else if (inByte == ' ') {
      pos++;
      if (pos >= 4) pos = 0;
    }
    else if (inByte == ',' || inByte == 'n') {
      setLED(in[0], in[1], in[2], in[3]);
      /*
      Serial.print('[', BYTE);
      Serial.print(in[0], DEC);
      Serial.print(',', BYTE);
      Serial.print(in[1], DEC);
      Serial.print(',', BYTE);
      Serial.print(in[2], DEC);
      Serial.print(',', BYTE);
      Serial.print(in[3], DEC);
      Serial.print(']', BYTE);
      */
      pos = 0;
      in[0] = 0;
      in[1] = 0;
      in[2] = 0;
      in[3] = 0;
    }
    else if (inByte == 'W') {
      WriteLEDArray();
     // Serial.print('!', BYTE);
      pos = 0;
    }
    else if (inByte == 'C') {
      clearLEDs();
      pos = 0;
    }
    //Serial.print(inByte, BYTE);
    
    
   }
   
   
   /*
  int i;
  static int x, y, z;
  
  for (i = 1; i < 8; i++)
  {
    setLED(i, 0, 0, 0);
  }
  
  setLED(x, 1023, 1023, 1023);
  x++;
  if (x > 7)
    x = 1;
  WriteLEDArray();
  delay(500);
 
 */
}

