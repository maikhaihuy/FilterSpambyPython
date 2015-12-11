import naive_bayes
import scipy.io

# 1. TRAIN
# 1.1. Load training data
print 'Load training data ...'
training_data = scipy.io.loadmat('spamTrain.mat')
#print training_data
X = training_data['X']
y = training_data['y']
print 'X.shape =', X.shape
print 'y.shape =', y.shape

# 1.2. Train Naive Bayes classifier
print 'Train Naive Bayes classifier ...'
phi, phi0, phi1 = naive_bayes.train(X, y)
print 'phi =', phi
print 'phi0[0:10] =', phi0[0:10]
print 'phi1[0:10] =', phi1[0:10]

# 2. TEST
# 2.1. Load test data
print 'Load test data ...'
test_data = scipy.io.loadmat('spamTest.mat')
X_test = test_data['Xtest']
y_test = test_data['ytest']
print 'X_test.shape =', X_test.shape
print 'y_test.shape =', y_test.shape

# 2.2. Test Naive Bayes classifier
print 'Test Naive Bayes classifier ...'
acc = naive_bayes.test(phi, phi0, phi1, X_test, y_test)
print 'Accuracy =', acc