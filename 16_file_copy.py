#copy the content of one file into another

from sys import argv
from os.path import exists

thisscriptsname, src_filename, dest_filename= argv

if exists(src_filename) and exists(dest_filename):
    src_content = open(src_filename, "r").read()
    open(dest_filename,"w").write(src_content)
else:
    print "either %s or %s doesn't exist !" %(src_filename, dest_filename)


