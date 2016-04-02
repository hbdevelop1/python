
from sys import argv
thisscriptsname, filename = argv

print "the contect of %s is:" % filename
file_data = open(filename)
print file_data.read()

