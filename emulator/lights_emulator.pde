/**
 * oscP5sendreceive by andreas schlegel
 * example shows how to send and receive osc messages.
 * oscP5 website at http://www.sojamo.de/oscP5
 */
 
import oscP5.*;
import netP5.*;
  
OscP5 oscP5;
int numboxes = 24;
color[] colors = new color[numboxes];

void setup() {
  size(1000,200);
  frameRate(60);
  /* start oscP5, listening for incoming messages at port 12000 */
  oscP5 = new OscP5(this,11661);
  
}


void draw() {
  background(0);  
  
  
  float boxwidth = width/numboxes;
  for (int i=0; i<numboxes; i++) {
    fill(colors[i]);
    rect(i*boxwidth, 0, boxwidth, height);
  }
  
}



/* incoming osc message are forwarded to the oscEvent method. */
void oscEvent(OscMessage theOscMessage) {
  /* print the address pattern and the typetag of the received OscMessage */
  print("### received an osc message.");
  print(" addrpattern: "+theOscMessage.addrPattern());
  println(" typetag: "+theOscMessage.typetag());
  int len = theOscMessage.arguments().length;
  for (int i=0; i<min(len/3, numboxes); i++) {
      int r = theOscMessage.get(i*3+0).intValue() / 4;
      int g = theOscMessage.get(i*3+1).intValue() / 4;
      int b = theOscMessage.get(i*3+2).intValue() / 4;
      colors[i] = color(r,g,b);
      println("Color: "+r+","+g+","+b+".");
  }
}
