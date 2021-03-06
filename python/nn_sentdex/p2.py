inputs = [1, 2, 3, 2.5]
weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]
bias1 = 2
bias2 = 3
bias3 = 0.5

# output = input * weights + bias --> basic neural network with 3 inputs & 1 output
# consider this as a single neuron with 3 inputs and one output -->
# 3 weights needed to translaet the input to output
# Inputs can be value from input layer or they can be input to a hidden layer.

# Handcoding a 4 input 3 neuron layer.
output1 = inputs[0] * weights1[0] + inputs[1] * \
    weights1[1] + inputs[2] * weights1[2] + inputs[3] * weights1[3] + bias1
output2 = inputs[0] * weights2[0] + inputs[1] * \
    weights2[1] + inputs[2] * weights2[2] + inputs[3] * weights2[3] + bias2
output3 = inputs[0] * weights3[0] + inputs[1] * \
    weights3[1] + inputs[2] * weights3[2] + inputs[3] * weights3[3] + bias3

output = [output1, output2, output3]
print(output)
