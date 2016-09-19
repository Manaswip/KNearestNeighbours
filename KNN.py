import ExtractingData as e
import numpy as np
from numpy import linalg as LA

""" In KNN there is no training time. Each time we get a new image, in order to
find label of the image: calculate k nearest neighbours, then the label if the image
will be the label dominant in those K neighbours
"""

#Loading training data
X,y,rows,cols = e.ExtractingData()
#Loading test data
X_test,y_test,rows_test,cols_test =  e.ExtractingTestData()
#number of training samples
m = X.shape[0]
#number of testing samples
m_test = X_test.shape[0]
# Initializing variables
input_layer_size  = rows*cols;  # 28x28 Input Images of Digits
num_labels = 10;          # 10 labels, from 0 to 9  
k = 11;


allDistances = np.zeros((m_test,m));

for i in range(0,m_test):
	for j in range(0,m):
		allDistances.itemset((i,j),LA.norm(X_test[i]-X[j]));

allDistances=allDistances.astype(float)
np.save('distances',allDistances)
#allDistances = np.load('distances.npy')

nearest = np.zeros((m_test,k));
values = np.zeros((m_test,k));
predict = np.zeros((m_test,1))

nearest = np.argpartition(allDistances,k)[:,0:k]

values=y[nearest]

for j in range(0,m_test):
	C,indices = np.unique(values[j],return_inverse=True);
	predict.itemset((j,0),C[np.argmax(np.bincount(indices),0)]);

#How many were predicted correctly
A = (predict == y_test)
np.uint8(A)

#83.92 accuracy 11 neighbours
print "Training Accuracy:", np.mean(A)*100