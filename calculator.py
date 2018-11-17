import turtle;
import random;
from os import system;


memory = [];
pen = turtle.Turtle();
pen.speed = 100000000000000000000000000000000000000000000000000000000000;
win = pen.getscreen();
pen.setx(0);
pen.sety(0);
display = "";
buttons = [];
tooutput = "";

def createline():
  global pen;
  i = 0;
  while i < len(display):
    pen.forward(12);
    i = i+1;
  i = 0;
  while i < len(display):
    pen.backward(12);
    i = i+1;

def updatetext():
  pen.clear();
  pen.write(display, font = ("arial",16,"bold"));


def output(text):
  global tooutput;
  tooutput = text;

def calculate():
  global display;
  args = str.split(display,' ');
  try:
    temp = float(args[0]);
  except:
    temp = random.randint(0,100);
  i = 0;
  print(args);
  while i < len(args):
    try:
      if args[i] == "*":
        temp = temp * float(args[i+1]);
      if args[i] == "/":
        temp = temp / float(args[i+1]);
      if args[i] == "-":
        temp = temp - float(args[i+1]);
      if args[i] == "+":
        temp = temp + float(args[i+1]);
      if args[i] == "^":
        temp = pow(temp,float(args[i+1]));
      if args[i] == "?":
        args[i] = random.randint(0,1000); 
    except:
      output("An unexpected system error has occured. Here are some possible causes.\nSyntax Error\nBad Input\nSystem Bug");
      break;
    i = i+1;
  display = str(temp)
  updatetext();
  createline();

def click(x,y):
  global display;
  for button in buttons:
    if button.clicked(x,y)==True:
      if button.text == "=":
        calculate();
        return;
      if button.text == "<":
        output("Clearing");
        display = "";
        updatetext();
        return;
      if button.text == "M+":
        memory.append(display);
        display = "Dat rec to slot "+str(len(memory)-1);
        updatetext();
        return;
      if button.text == "M-":
        try:
          memory[int(display)] = "Slot Mem Deleted"
        except:
          display = "Cannot find slot";
          updatetext();
        return;
      if button.text == "MRC":
        try:
          display = memory[int(display)];
          updatetext();
          return;
        except:
          display = "Cannot find slot";
          updatetext();
          return;

      display = display + button.text;
      updatetext();

class button(object):
  x = 0;
  y = 0;
  w = 100;
  h = 100;
  text = "";
  def clicked(self,x,y):
    if x > self.x and x < (self.x+self.w) and y > self.y and y < (self.y+self.h):
      return True;

    return False;

  def draw(self,turtle):
    turtle.sety(self.y);
    turtle.setx(self.x);
    turtle.clear();
    turtle.write(self.text, font = ("arial",16,"bold"));
    turtle.forward(self.w);
    turtle.left(90);
    turtle.forward(self.h);
    turtle.left(90);
    turtle.forward(self.w);
    turtle.left(90);
    turtle.forward(self.h);
    turtle.left(90);

def addbutton(x,y,w,h,text):
  turd = turtle.Turtle();
  temp = button();
  turd.speed = 100000000000000000000000000000000000000000000000000;
  turd.hideturtle();
  temp.text = str(text);
  temp.y = y;
  temp.x = x;
  temp.w = w;
  temp.h = h;
  temp.draw(turd);
  buttons.append(temp);

def renderbuttons():
  i = 0;
  while i < 10:
    addbutton(int(i*20),-30,20,20,i);
    i = i+1;
  addbutton(int(i*20),-30,20,20,".")
  addbutton(0,-60,20,20," * ");
  addbutton(20,-60,20,20," / ")
  addbutton(40,-60,20,20," + ");
  addbutton(60,-60,20,20," - ")
  addbutton(80,-60,20,20,"<")
  addbutton(100,-60,20,20,"=")
 
def addfunctions():
  addbutton(120,-60,30,20,"M+");
  addbutton(150,-60,30,20,"M-");
  addbutton(180,-60,50,20,"MRC");
  addbutton(0,-90,20,20," ^ ")
  addbutton(20,-90,20,20,",")
  addbutton(40,-90,20,20,"?");

def drawhelp():
  infile = open("help.txt","r");
  tur = turtle.Turtle();
  tur.setx(-300);
  tur.sety(0);
  tur.clear();
  tur.write(infile.read(),font=("Arial",11));
  infile.close();
  
def update():
  tur = turtle.Turtle();
  tur.setx(100);
  tur.sety(0);
  tur.clear();

drawhelp();
renderbuttons();
win.onclick(click);
createline();
addfunctions();
print("Calculator 1.0");
print("(C) Michael Wang")
print("The help guide is on the turtle window. For desired graphics quality, please don't resize the window");
