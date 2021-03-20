import numpy as np


class Perceptron(object):
    
    def __init__(self, no_of_inputs, threshold=100, learning_rate=0.01):
        self.threshold=threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_inputs + 1)
        
    def predict(self, inputs):
        summation=np.dot(inputs, self.weights[1:]) + self.weights[0]
        if summation>0:
            activation=1
        else:
            activation=0
        return activation
    
    def train(self, training_inputs, labels):
        for x in range(self.threshold):
            for inputs, label in zip(training_inputs, labels):
                prediction=self.predict(inputs)
                self.weights[1:]+= self.learning_rate * (label-prediction) * inputs
                self.weights[0] += self.learning_rate * (label-prediction)
                print("error for ",x," epoch--> ",label-prediction)
              # print(self.weights[1:])
            if self.predict(np.array([1,1]))==1 and self.predict(np.array([1,0]))==0 and self.predict(np.array([0,1]))==0 and self.predict(np.array([0,0]))==0 :                
               print("minimum threshold -->",x)
               break
        