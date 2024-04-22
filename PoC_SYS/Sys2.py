import sys

def main():
    if(len(sys.argv<3)):
     sys.stderr.write("E: usage: "+sya.argv[0]+"<filename <word>>")
     sys.stderr.flush
     exit(2)
    else:
     filename=sys.argv[1]
     needle = sys.argv[2]
    

    with open(filename) as robj:
        content=robj.read()
        print(content)
