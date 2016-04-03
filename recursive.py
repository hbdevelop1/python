print "hello"
def recursive_fn(a):
    print a
    if a < 1:
        return
    else:
        recursive_fn(a-1)
    
recursive_fn(4)
