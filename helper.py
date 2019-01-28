class Image():
    def __init__(self, X, Y, Z = 3):
        self.X = X
        self.Y = Y
        self.Z = Z

    def applykernel(self, kernel, stride, padding):
        self.X = (self.X - kernel.X + 2*padding)/stride + 1
        self.Y = (self.Y - kernel.Y + 2*padding)/stride + 1
        print("Image Dimension is now {}, {} ".format(self.X, self.Y))
        se
    def applypooling(self, pool_size, stride):
        # Reffered from http://cs231n.github.io/convolutional-networks/#pool
        self.X = (self.X - pool_size)/(stride) + 1
        self.Y = (self.Y - pool_size)/(stride) + 1

        
    def padding():    
        pass

class kernel():
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

