import numpy;

def sigmoid(x):
	return 1 / (1 + numpy.exp(-x));

def derivSigmoid(x):
	return x*(1-x);

# input data
training_input = numpy.array([
	[0, 0, 1],
	[1, 1, 1], 
	[1, 0, 1], 
	[0, 1, 1]
])

# out data
training_expected_output = numpy.array([
	[0, 1, 1, 0]
]).T

# weights 
weight = 2*numpy.random.random((3,1)) - 1

# training
for item in range(10000):
	weighted_input = numpy.dot(training_input, weight);
	
	# the data is bound within 0 - 1
	# therefore sigmoid function would be used
	training_output = sigmoid(weighted_input);
	error = training_expected_output - training_output
	
	# the derivation of sigmoid function would be used as the rate of learning
	rateOfLearning = derivSigmoid(training_output);
	delta = error * rateOfLearning
	learned = numpy.dot(training_input.T, delta)
	weight += learned ;


print("Trained Weight")
print(weight)

print("Input")
print(training_input[0])

print("Expected Outptut")
print(training_expected_output[0])

print("Outptut")
print(sigmoid(numpy.dot(training_input[0], weight)))