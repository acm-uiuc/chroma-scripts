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
PFont f;
boolean displayText = true;
boolean debugText = false;

void setup() {
  size(400, 600);
  frameRate(60);
  f = loadFont("AmericanTypewriter-48.vlw");
  textFont(f, 48);
  /* start oscP5, listening for incoming messages at port 12000 */
  oscP5 = new OscP5(this, 11661);
  usage();
}

void usage() {
  println("lights_emulator: \n\t t - toggle text\n\t d - debug text");
}

int[] actualorder = {
  16, 17, 18, 19, 20, 21, 22, 23, 8, 9, 10, 11, 12, 13, 14, 15, 2, 3, 4, 5, 6, 0, 1, 7
};
void draw() {
  background(0);
  float boxwidth = 100; //hard coded!
  for (int i=0; i<24; i++) {
    int a = actualorder[i];
    int column = i%4;
    int row = i/4;
    fill(colors[a]);
    rect(column*boxwidth, row*boxwidth, boxwidth, boxwidth);
    if (displayText) {
      fill(255, 140);
      textFont(f, 48);
      textAlign(CENTER, CENTER);
      text(""+(i), column*boxwidth+boxwidth/2, row*boxwidth+boxwidth/2);
    }
    if (debugText) {
      textFont(f, 20);
      textAlign(RIGHT, BOTTOM);
      text(""+(a), (column+1)*boxwidth-3, (row+1)*boxwidth-3);
    }
  }
}


void keyPressed() {
  if (key == 't') {
    displayText = !displayText;
  } 
  else if (key == 'd') {
    debugText = !debugText;
  }
}




/* incoming osc message are forwarded to the oscEvent method. */
void oscEvent(OscMessage theOscMessage) {
  try {
    /* print the address pattern and the typetag of the received OscMessage */
    print("### received an osc message.");
    print(" addrpattern: "+theOscMessage.addrPattern());
    println(" typetag: "+theOscMessage.typetag());
    int len = theOscMessage.arguments().length;
    for (int i=0; i<min(len/3, numboxes); i++) {
      int r = int(theOscMessage.get(i*3+0).floatValue() / 4);
      int g = int(theOscMessage.get(i*3+1).floatValue() / 4);
      int b = int(theOscMessage.get(i*3+2).floatValue() / 4);
      colors[i] = color(r, g, b);
      //println("Color: "+r+","+g+","+b+".");
    }
  } 
  catch (Exception e) {
    e.printStackTrace();
  }
}

