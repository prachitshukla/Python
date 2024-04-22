import sys

myName='Prachit Shukla'
print(f"My name is {myName}".center(50,'*'),'#test center function')

#print("Input dir to read the files from".center(printmainfillinglen,printmainfillingchar),srcdir)


print(sys.copyright)
print("Where the python is : ",sys.executable)
print(sys.version)
print('*'.center(80,'*'))
print(print(sys.builtin_module_names))

print("check for module name : time ", sys.modules.keys)

print('')
print('Plateform Name is : '.center(50,'*'),sys.platform)


print('')
print('sysversion name is : '.center(50,'*'),sys.getwindowsversion())

import string
import re

def main():
    print("i am in main")
    name=input('what is your name : ')
    #for digit in string.digits:
       # if (digit in name):
    if(re.search('\d',name)):
            sys.stderr.write("you have numbers in your name")
            sys.stderr.flush()
    else:
        print(f'its good to meet you {name}')

print('')
if (__name__=='__main__'):
    main();

