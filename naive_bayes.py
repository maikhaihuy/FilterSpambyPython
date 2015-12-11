import numpy as np

def train(X, y):
	'''
	This function trains a Naive Bayes classifier.
	
	Parameters:
	-----------
	X: The matrix in which the ith row corresponds to the ith input vector of ith training 
	   example (each training example contains input vector and correct output); its shape 
	   is (<# training examples>, <# dimensions of input space>).
	y: The vector (actually the matrix whose shape is (<# training examples>, 1)) in which 
	   the ith element corresponds to the ith correct output of ith training example.
	
	Returns:
	--------
	(Here I just describe the shapes of returned variables. Please read the pdf file for the
	meaning of these variables.)
	phi: a scalar.
	phi0: a vector whose shape is (<# dimensions of input space>,).
	phi1: a vector whose shape is (<# dimensions of input space>,). 
	'''
	
	# TODO 
	return (0, np.zeros(X.shape[0]), np.zeros(X.shape[0]))

def predict_spam(phi, phi0, phi1, X_test):
	'''
	This function predicts whether an email is spam using the trained Naive Bayes classifier.
	
	Parameters:
	
	-----------
	phi, phi0, phi1: Parameters of the trained Naive Bayes classifier.
	X_test: The matrix in which the ith row corresponds to the ith test input vector.
	
	Returns:
	--------
	A vector in which the ith element corresponds to the prediction of ith test input vector. 
	'''
	
	# TODO
	return np.zeros(X_test.shape[0])

def test(phi, phi0, phi1, X_test, y_test):
	'''
	This function tests the trained Naive Bayes classifier.
	
	Parameters:
	-----------
	phi, phi0, phi1: Parameters of the trained Naive Bayes classifier.
	X_test: The matrix in which the ith row corresponds to the ith input vector of ith test 
	        example (each test example contains input vector and correct output); its shape 
	        is (<# test examples>, <# dimensions of input space>).
	y_test: The vector (actually the matrix whose shape is (<# test examples>, 1)) in which 
	        ith element corresponds to the ith correct output of ith test example.
	
	Returns:
	--------
	The accuracy (in [0, 1]) of the trained Naive Bayes classifier on the test data. 
	'''
	
	# TODO
	return 0