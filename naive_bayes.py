import numpy as np
import math

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
	# Cal phi
	phi = 0.0
	vecLabelMail = y[:, 0]
	arrSpam = [1 for x in vecLabelMail if x == 1]
	phi = len(arrSpam)*1.0/len(vecLabelMail)

	# Cal phi0 and phi1
	phi0 = []
	phi1 = []
	for vecMaili in X.T:
		arrNumeratorPhi0 = [1]
		arrNumeratorPhi1 = [1]

		arrNumeratorPhi0 = [1 for m, l in zip(vecMaili, vecLabelMail) if m == 1 and l == 0]
		arrNumeratorPhi1 = [1 for m, l in zip(vecMaili, vecLabelMail) if m == 1 and l == 1]

		denominatorPhi0 = 2.0 + len(vecLabelMail) - len(arrSpam)
		denominatorPhi1 = 2.0 + len(arrSpam)

		phi0.append(((len(arrNumeratorPhi0) + 1)/(denominatorPhi0)))
		phi1.append(((len(arrNumeratorPhi1) + 1)/(denominatorPhi1)))

	return (phi, phi0, phi1)

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
	x_label = []
	for vecVocaOfMail in X_test[:,]:
		label1 = 0.0
		label0 = 0.0
		for m, p1, p0 in zip(vecVocaOfMail, phi1, phi0):
			label1 = label1 + math.log10(m*p1 + (1-m)*(1-p1))
			label0 = label0 + math.log10(m*p0 + (1-m)*(1-p0))

		label1 = label1 + math.log10(phi)
		label0 = label0 + math.log10(1 - phi)
		print "1 ", label1
		print "0 ", label0
		x_label.append(0 if label1 < label0 else 1)

	return x_label

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
	y_label = predict_spam(phi, phi0, phi1, X_test)
	return 0