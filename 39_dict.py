#dictionary/map : keys(), item()
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

print "the known states are"
for state in states.keys():
    print state

for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

