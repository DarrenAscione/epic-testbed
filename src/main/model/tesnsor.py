import tensorflow as tf

class CNN:

	def __init__(self, alpha, training_iter, batch_size, display_step):
		self.alpha = alpha
		self.training_iter = training_iter
		self.batch_size = batch_size
		self.display_step = display_step
		self.x = tf.placeholder("float", [None, 784])
		self.y = tf.placeholder("float", [None, 10])

	def model(self):

		# set weights
		W = tf.Variable(tf.zeros([784,10]))
		b = tf.Variable(tf.zeros([10]))

		with tf.name_scope("Wx_b") as scope:
			cnn_model = tf.nn.softmax(tf.matmul(self.x, W) + b)

		w_h = tf.histogram_summary("weights", W)
		b_h = tf.histogram_summary("biases", b) 

		with tf.name_scope("cost_function") as scope:
		    # Minimize error using cross entropy
		    cost_function = -tf.reduce_sum(y*tf.log(model))
		    # Create a summary to monitor the cost function
		    tf.scalar_summary("cost_function", cost_function)

		with tf.name_scope("train") as scope:
		    # Gradient descent
		    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost_function)

		# Initializing the variables
		init = tf.initialize_all_variables()

		# Merge all summaries into a single operator
		merged_summary_op = tf.merge_all_summaries()

		# Launch the graph
		with tf.Session() as sess:
		    sess.run(init)

#cnn = CNN(0.01, 30, 100, 2)
#cnn.model()
