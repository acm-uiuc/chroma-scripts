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

boolean displayText = true;

void setup() {
  size(400,600);
  frameRate(60);
  PFont f = loadFont("AmericanTypewriter-48.vlw");
  textFont(f,48);
  textAlign(CENTER, CENTER);
  /* start oscP5, listening for incoming messages at port 12000 */
  oscP5 = new OscP5(this,11661);
  usage();
}

void usage() {
  println("lights_emulator: \n\t t - toggle text");
}


void draw() {
  background(0);
  float boxwidth = 100; //hard coded!
  for (int i=0; i<16; i++) {
    int column = i%4;
    int row = i/4;
    fill(colors[i]);
    rect(column*boxwidth, row*boxwidth, boxwidth, boxwidth);
    if (displayText) {
      fill(255, 140);
      text(""+i, column*boxwidth+boxwidth/2, row*boxwidth+boxwidth/2);
    }
  }
  for (int i=18; i<23; i++) {
    int j = i-2;
    int column = j%4;
    int row = j/4;
    fill(colors[i]);
    rect(column*boxwidth, row*boxwidth, boxwidth, boxwidth);
    if (displayText) {
      fill(255, 140);
      text(""+j, column*boxwidth+boxwidth/2, row*boxwidth+boxwidth/2);
    }
  }
}


void keyPressed() {
  if (key == 't') {
    displayText = !displayText;
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
        colors[i] = color(r,g,b);
        println("Color: "+r+","+g+","+b+".");
    }
  } catch (Exception e) {
    e.printStackTrace();
  }
}
