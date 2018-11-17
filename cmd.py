from os import system;

inp = "";

system("cd C:");
system("title Command Prompt");
       
while inp != "exit":
  inp = input(">");
  system(inp);
