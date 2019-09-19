import numpy as np



class ANN:

    def __init__(self, type= None, optimizer = None, initial_W = 0):
        self.layers = []
        self.type = type
        self.optimizer = optimizer
        self.depth = 0
        self.initial_W = initial_W



    def add_layer(self, m, n, Activation):
        self.layers.append(Layer(M = m, N = n, activation = Activation, level = self.depth))
        self.layers[self.depth].W = np.full((self.layers[self.depth].M, self.layers[self.depth].N), self.initial_W)
        self.depth += 1

    def check_ANN(self):
        if self.type == None:
            if self.optimizer == None:
                if self.depth == 0:
                    print("Fault ANN: type is:",  self.type, "optimizer is:", self.optimizer, "depth must be greater than", self.depth, "\n\n")
                    return False
        elif self.optimizer == None:
            if self.depth == 0:
                print("Fault ANN: optimizer is:", self.optimizer, "depth must be greater than",
                      self.depth, "\n\n")
                return False
        elif self.type == None:
            if self.depth == 0:
                print("Fault ANN: type is:",  self.type, "depth must be greater than", self.depth, "\n\n")
                return False
        elif self.depth == 0:
            print("Fault ANN: depth must be greater than", self.depth, "\n\n")
            return False
        else:
            return True

    def check_Layers(self):
        return True

    def compile(self):
        check_ANN()
        check_Layers()

class Layer(object):

    def __init__(self, M = None, N = None, bias = False, set_bias = 1, activation = None, W = None, level = None):
        self.M = M
        self.N = N
        self.W = W
        self.bias = bias
        self.set_bias = set_bias
        self.activation = activation
        self.level = level




model = ANN(type = "forward footing", optimizer = "SGD")

model.add_layer(m = 13, n =12, Activation = 'relu')

