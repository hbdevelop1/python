
class Point(object):
    def __init__(self, _x=0, _y=0):
        self.x=_x
        self.y=_y
        
    def printo(self):
        print "the point is(%d,%d)" %(self.x,self.y)
