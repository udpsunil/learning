import tensorflow as tf

"""
A tensor is a generalization of vectors and matrices to potentially higher dimensions.
"""
# creating tensors
string = tf.Variable("this is a string", tf.string)
number = tf.Variable(42, tf.int16)
floating = tf.Variable(3.1415, tf.float64)

# rank or degree of tensor
rank1_tensor = tf.Variable(["Test"], tf.string)
rank2_tensor = tf.Variable([["Test", "Ok"], ["Test", "Nok"]], tf.string)

print(tf.rank(rank1_tensor))
print(tf.rank(rank2_tensor))

# shape of a tensor
print(rank1_tensor.shape)
print(rank2_tensor.shape)

# changing shape
tensor1 = tf.ones([1, 2, 3])
print(tensor1)
tensor2 = tf.reshape(tensor1, [2, 3, 1])
print(tensor2)
tensor3 = tf.reshape(tensor2, [3, -1])
print(tensor3)

tensor = tf.zeros([5, 5, 5, 5])
print(tensor)
tensor = tf.reshape(tensor, [625])
print(tensor)
tensor = tf.reshape(tensor, [125, -1])
print(tensor)
