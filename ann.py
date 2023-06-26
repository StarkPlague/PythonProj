import csv
import tensorflow as tf
from sklearn.model_selection import train_test_split


# read the data from the CSV file
with open('heart.csv') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

# separate the input data and the labels
data_x = [row[:-1] for row in data]
data_y = [row[-1] for row in data]


X_train, X_test, y_train, y_test = train_test_split(
    data_x, data_y, random_state=7, train_size=.80)

# define the input data and the expected output
x = tf.placeholder(tf.float32, shape=[None, 2])
y = tf.placeholder(tf.float32, shape=[None, 1])

# define the model weights and biases
w1 = tf.Variable(tf.random_normal([2, 4]))
b1 = tf.Variable(tf.zeros([4]))
w2 = tf.Variable(tf.random_normal([4, 1]))
b2 = tf.Variable(tf.zeros([1]))

# define the model layers
layer1 = tf.nn.sigmoid(tf.matmul(x, w1) + b1)
output = tf.nn.sigmoid(tf.matmul(layer1, w2) + b2)

# define the loss function and the optimizer
loss = tf.reduce_mean(tf.square(output - y))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# create a session to run the model
with tf.Session() as sess:
    # initialize the model variables
    sess.run(tf.global_variables_initializer())

    # run the training loop
    for i in range(100):
        sess.run(train, feed_dict={x: data_x, y: data_y})

    # evaluate the model on some test data
    result = sess.run(output, feed_dict={x: X_test})
    print(result)
