# Casting-Defect-Detection-and-Classification-Model-using-CNN
A Machine learning model to detect defects in industrial pump impeller casts and classify the type of it.

**Abstract**

This work aims to develop a neural network to categorize the submersible pump impeller casts as defective or not. Nearly 7348 images of the casts provided by Pilot Technocast cast manufacturer are used. The model used here is Convolutional Neural Network (CNN). The activation function used is Relu. A two layered convolutional network is used with Conv2d and Maxpooling2d layers in it. This model is trained using the above dataset and is then used to classify new images with an accuracy of roughly 94%. This work also proposes a detect classification method which can identify the defect type.


The dataset used here is an image dataset which consists of 7348 images.  6633 images of 300X300 pixel size are used for training. There are two categories:
1. Defective
2. Non-defective

Another dataset is manually created by using the images from ‘Defective’ category with two categories i.e. the defect types.

1.Fins: A fin is any extra or undesirable material that is affixed to a cast. At the parting faces, this thin layer of metal often develops.

2.Heat cracks: The development of shrinkage cracks during the solidification of weld metal are known as heat cracks.

Figure 1 below illustrates the Algorithm's Block Diagram.


![image](https://user-images.githubusercontent.com/102479943/189540722-afe05f0e-dfb6-4701-8c34-19c6059621d5.png)


The availability of the defect is identified with a 94 percent accuracy rate, and the type of the defect is identified with a 68 percent accuracy rate. To test the prepared model, a distinct image set was employed that was never used elsewhere.

The first convolutional layer has eight filters with a three by three kernel size matrix. Reduce the image size by half by making 2-pixel steps at a time.

First pooling layer: By using the maximum pooling matrix (2 by 2) and 2-pixel strides sequentially, the image size is further reduced by half.

The first convolutional layer and the second layer are identical. The first pooling layer and the second pooling layers are also the same.

In order to be fed into the fully-connected layer, two-dimensional pixel data must be flattened into one dimension. In order to translate the scores into a chance that an image is defective, the output layer, which only has one unit, uses a sigmoid function for activation. With exception of the output layer, all layers use the Rectified Linear Unit (ReLU) activation function.


Figure 2 below illustrates the convolutional network's structure in usage.

 
![image](https://user-images.githubusercontent.com/102479943/189540834-8de9aa81-770f-4a82-b8b7-a549d885508e.png)


**Conclusion**

The model used here managed to classify the images has been sufficiently accurate in identifying the defects and also in increasing the type of defect found. This can be more efficient than the human supervision. But the accuracy can be further increased by using a better algorithm by using better computing resources. This can make the model usable in cast industrial level. The number of type of defects identified can also be increased and also use images of better quality to further increase the accuracy of the model.

