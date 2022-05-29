import numpy as np

class NeuralNetwork:
    def __init__(self,layers, alpha=0.1):
        self.W=[]
        self.layers=layers
        self.alpha=alpha
        
        for i in np.arange(0,len(layers) -2):
            w=np.random.rand(layers[i] +1, layers[i +1]+1)
            self.W.append(w / np.sqrt(layers[i]))
    
    
    def __repr__(self):
        return "Sieć neuronowa: {}".format(
            "-".join(str(l) for l in self.layers)
        )
    
    def sigmoid(self, x):
        return 1.0 / (1 + np.exp(-x))


    def sigmoid_deriv(self, x):
        return x * (1 - x)
    
    def fit(self,X,y,epochs=1000, displayUpdate=100):
        
        X=np.c_[X,np.ones((X.shape[0]))]
        
        for epoch in np.arange(0, epoch):
            for(x,target) in zip(X,y):
                self.fit_partial(x,target)
                
                if epoch ==0 or (epoch +1) % displayUpdate ==0:
                    loss =self.calculate_loss(X,y)
                    print("[INFO] epoka={}, strata={:.7f}"
                          .format(epoch+1, loss))
                    
    
        
        