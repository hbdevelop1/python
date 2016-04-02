#erase the content of a file and write 3 lines into it

from sys import argv
thisscriptsname, filenametowriteto= argv

filetowriteto = open(filenametowriteto, "w")

print "enter the content to write to the file:"
line1ToWrite=raw_input("line1:")
line2ToWrite=raw_input("line2:")
line3ToWrite=raw_input("line3:")

linebreak="\n"
filetowriteto.write(line1ToWrite+linebreak+line2ToWrite+linebreak+line3ToWrite+linebreak)

filetowriteto.close()
