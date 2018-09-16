class vector():

    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def getVectorX(self):
        return self.xpos

    def setVectorX(self, x):
        self.xpos = x

    def getVectorY(self):
        return self.ypos

    def setVectorY(self, y):
        self.ypos = y

    def getVector(self):
        return [self.xpos, self.ypos]

    def setVector(self, x, y):
        self.xpos = x
        self.ypos = y

    def addVector(self, v1, v2):
        self.xpos += v1
        self.ypos += v2
