from urllib import request;
from os import system;
import smtplib;

data = "";
url = "startpage";

infile = open("dump/page.py","w");
infile.write("\n Welcome to PyWeb v1.0\n(C) 2018 Michael Wang");
infile.close();

def navigate(urlpath):
    try:
        webFile = request.urlopen(urlpath).read();
        global url;
        if urlpath.find("PyNet") == -1:
            url = urlpath;
        else:
            url = "PyNetwork";
            
        infile = open("dump/page.py","wb");
        infile.write(webFile);
        infile.close();
        return 0;
    except:
        url = "Error";
        infile = open("dump/page.py","w");
        infile.write("An Error Has Occured\n-Make sure to type the site url correctly\n-Check your internet connection.\n\nOriginal Source:\n"+urlpath);
        infile.close();
        return 1;

def display():
    global data;
    global url;
    system("cls");
    infile = open("dump/page.py","r");
    data = infile.read();
    system("title PyWeb URL: "+url);
    print("PyWeb v1.0      (C) Michael Wang      URL: "+url+"\n");
    print(data+"\n\nPyNet and Pyweb (C) 2018 Michael Wang");
    infile.close();

userinp = "";
comargs = []
system("title PyWeb");
display();
while userinp !="exit":
    userinp = input(">");
    comargs = str.split(userinp," ");

    if comargs[0] == "nav":
        navigate(comargs[1]);
        display();

    if comargs[0] == "pynet":
        if comargs[1] == "about":
            navigate("https://raw.githubusercontent.com/TheRealMichaelWang/PyNet/master/README.md");
            display();
        if comargs[1] == "home":
            navigate("https://raw.githubusercontent.com/TheRealMichaelWang/PyNet/master/Home");
            display();
        if comargs[1] == "get":
            if navigate("https://raw.githubusercontent.com/TheRealMichaelWang/PyNet/files/"+comargs[2]) == 0:
                run = input("Would you like to view source or run?(v/r)");
                if run == "r": 
                    system("start dump/page.py");
                if run == "v":
                    display();
            else:
                display();
        
    if comargs[0] == "help":
        print("PyWeb Commands:\n-'nav' Navigates to a url\n-'pynet' Goes the PyNet Network\n-'os' pumps an os command");
        
    if comargs[0] == "os":
        system(comargs[1]);
    
    if comargs[0] == "cls" or comargs[0] == "clear":
        system("cls");
        system("title PyWeb");
