#list: list of list (bucket)

map1 = []

for i in range(0,10):
    map1.append([])
print map1    

bucket=map1[0]
bucket.append(("key1","value4key1"))
bucket.append(("key2","value4key2"))

print map1    

bucket[0]=("key1new","value4key1new")
print map1    

