class Planet:
    def __init__(self, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4):
       self.x1 = x1
       self.y1 = y1
       self.z1 = z1
       self.x2 = x2
       self.y2 = y2
       self.z2 = z2
       self.x3 = x3
       self.y3 = y3
       self.z3 = z3
       self.x4 = x4
       self.y4 = y4
       self.z4 = z4
    def disp(self):
        print(self.x1, self.y1, self.z1, self.x2, self.y2, self.z2, self.x3, self.y3, self.z3, self.x4, self.y4, self.z4)

Top = []
Bottom = []
Left = []
Right = []
Front = []
Back = []

back_1 = Back.append(Planet(5,5,0, 5,-5,0, -5,-5,0, -5,5,0))

##front_def = Planet(-4,5,1, -4,4,1, -5,4,1, -5,5,1)
##Front.append(front_def)

##left_def = Planet(-5,5,1, -5,4,1, -5,4,0, -5,5,0)
##Left.append(left_def)

##right_def = Planet(-4,5,0, -4,4,0, -4,4,1, -4,5,1)
##Right.append(right_def)

##top_def = Planet(-4,5,0, -4,5,1, -5,5,1, -5,5,0)
##Top.append(top_def)

##bottom_def = Planet(-4,4,0, -4,4,1, -5,4,1, -5,4,0)
##Bottom.append(bottom_def)

