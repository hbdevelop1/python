
from sys import argv
thisscriptsname, filename = argv

print "the contect of %s is:" % filename
file_data = open(filename)
print 2, file_data.readline()

