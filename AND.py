import numpy as np
from perceptron import Perceptron

training_inputs=[]
training_inputs.append(np.array([1,1]))
training_inputs.append(np.array([1,0]))
training_inputs.append(np.array([0,1]))
training_inputs.append(np.array([0,0]))

labels= np.array([1,0,0,0])

perceptron=Perceptron(2)
perceptron.train(training_inputs, labels)

test_input=np.array([1,1])
print("---------------------------------")
print(perceptron.predict(test_input))