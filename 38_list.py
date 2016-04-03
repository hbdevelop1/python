
#list:join, range in list, enumerate
names = ["aa", "bb", "Song", "Frisbee", "Corn", "Banana", "Girl"]
print names[6:19]  #print what ever it can
print '---'.join(names)
longstring=''.join(names[0:3])
print longstring

print ","*20
for i, item in enumerate(names):
    print i,",",item
