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



Figure 2 below illustrates the convolutional network's structure in usage.

 
![image](https://user-images.githubusercontent.com/102479943/189540834-8de9aa81-770f-4a82-b8b7-a549d885508e.png)


**Conclusion**

The model used here managed to classify the images has been sufficiently accurate in identifying the defects and also in increasing the type of defect found. This can be more efficient than the human supervision. But the accuracy can be further increased by using a better algorithm by using better computing resources. This can make the model usable in cast industrial level. The number of type of defects identified can also be increased and also use images of better quality to further increase the accuracy of the model.

