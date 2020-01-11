import os
from glob import glob
# Command Line Interface File Manager (clifm)
def ls():
    for i in range(0,len(os.listdir(os.curdir))):
        print(os.listdir(os.curdir)[i])
def echo(args):
    print(args)
def newfi(name):
    file = open(name, "w")
    file.close()
def newfo(name):
    os.mkdir(name)
def cd(name):
    os.chdir(name)
def chdr(name):
    os.chdir(name)
def chdir(name):
    os.chdir(name)
def inter(stri):
    parsed = stri.split()
    stria = ""
    if parsed[0] == "echo" or parsed[0] == "print":
        echo(" ".join(parsed[1:len(parsed)]))
    elif parsed[0] == "ls" or parsed[0] == "dir":
        ls()
    else:
        parsedargs = parsed[1:len(parsed)]
        exec(parsed[0]+"(\""+"".join(parsedargs)+"\")")
def cli():
    while True:
        inl = input(os.getcwd() + ">")
        inter(inl)
cli()
        
