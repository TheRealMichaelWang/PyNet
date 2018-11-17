from urllib import request;
from os import system;
data = "";
encoding = "utf-8";
url = "startpage";
infile = open("page.txt","w");
infile.write("\n Welcome to PyWeb v1.0\n(C) 2018 Michael Wang");
infile.close();

def navigate(urlpath):
    try:
        webFile = request.urlopen(urlpath).read();
        global url;
        if "github" not in url:
            url = urlpath;
        else:
            url = "PyNetwork";
        infile = open("page.txt","wb");
        infile.write(webFile);
        infile.close();
    except:
        url = "Error";
        infile = open("page.txt","w");
        infile.write("An Error Has Occured\n-Make sure to type the site url correctly\n-Check your internet connection.\n\nOriginal Source:\n"+urlpath);
        infile.close();

def display():
    global data;
    global url;
    system("cls");
    infile = open("page.txt","r");
    data = infile.read();
    print("PyWeb v1.0      (C) Michael Wang      URL: "+url+"\n");
    print(data);
    infile.close();

userinp = "";
comargs = []
system("title PyWeb");
display();
while userinp !="exit":
    userinp = input(">");
    comargs = str.split(userinp," ");
    display();

    if comargs[0] == "nav":
        navigate(comargs[1]);
        display();

    if comargs[0] == "pynet":
        if comargs[1] == "about":
            navigate("https://raw.githubusercontent.com/TheRealMichaelWang/PyNet/master/README.md");
        if comargs[1] == "home":
            navigate("https://raw.githubusercontent.com/TheRealMichaelWang/PyNet/master/Home");
        if comargs[1] == "get":
            navigate("https://raw.githubusercontent.com/TheRealMichaelWang/PyNet/master/"+comargs[2]);
        display();
