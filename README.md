<html>
<body>
<h3> Little bit about K-Nearest Neighbours </h3>
<p> k-nearest neighbours is a non-paramteric algorithm used for classification and regression. To algorithm, we input 
k closest training examples in feature space and the output is a class membership. An object is assigned to class most commmon
among its k neighbours.
</p>
<h3> K-Nearest Neighbours for classifying MNIST datset </h3>
<p>
<b>ExtractingData.py:</b> unpacks training images, training labels, testing images, and testing labels  from 'train-images-idx3-ubyte',
'train-labels-idx1-ubyte', 't10k-images-idx3-ubyte', 't10k-labels-idx1-ubyte' respectively. </br>
<b>KNN.py:</b> For every image in the testing dataset program calculates distances to all the images in training data and selects 
k nearest neighbours and classifies the new image to the class which is common among those k neighbours.
<h3>Accuracy </h3>
Accuracy is about 84% which is low, this is mainly because each image in MNIST dataset is normalized to 20x20 pixels which means each image has 400 features and as the dimensionality of features increase there is there is <a href="https://en.wikipedia.org/wiki/Curse_of_dimensionality">
curse of dimensionality</a> while calulating distance to its neighbours

</p>
</body>
</html>

 
