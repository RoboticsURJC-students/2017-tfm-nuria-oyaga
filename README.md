# 2017-tfm-nuria-oyaga
## Recurrent Neural Networks - LSTM
Once we have tested the prediction with simple networks without recurrences, we start to train, with the same data, networks that incorporate recurrence. In particular, we will focus the work on the LSTM networks helping us with the tutorials of

### Linear Functions dataset

## Non-Recurrent Neural Networks
The first step was to try to solve the problem of prediction with a classical neural network that does not use recurrence. We carry out the training of different networks with the generated data.

### Linear Functions dataset
The first thing we must do to train the network for prediction is to resize the data to ensure that the input shape is correct. For the function data we must have the following shapes:

```ruby
  input_shape=(n_samples, know_points=20, 1)
  output_shape = 1
```

For this type of data we have trained a simple MLP whose structure can be seen in the following figure:
<p align="center">
  <img width="280" src="https://github.com/RoboticsURJC-students/2017-tfm-nuria-oyaga/blob/master/docs/Models/Non-Recurrent/Linear_function/15_False_relu_mean_squared_error_10_properties.png">
</p>
As you can see in the following image, the network manages to reduce and stabilize the loss function in only a few epochs, obtaining a very reduced error.
<p align="center">
  <img width="450" src="https://github.com/RoboticsURJC-students/2017-tfm-nuria-oyaga/blob/master/docs/Models/Non-Recurrent/Linear_function/15_False_relu_mean_squared_error_10_history.png">
</p>
<p align="center">
  <img width="600" src="https://github.com/RoboticsURJC-students/2017-tfm-nuria-oyaga/blob/master/docs/Models/Non-Recurrent/Linear_function/15_False_relu_mean_squared_error_10_error_hist.png">
</p>
In the next image you can see the samples where the errors (absolute and relative) are maximum. In the case of relative error, when the line has a small slope the relative error is very high, this is because we divide by a very small value.

<p align="center">
  <img width="400" src="https://github.com/RoboticsURJC-students/2017-tfm-nuria-oyaga/blob/master/docs/Models/Non-Recurrent/Linear_function/15_False_relu_mean_squared_error_10_max_error.png">
</p>

### URM Vectors dataset
As in the functions case, the first thing we must do to train the network for prediction is to resize the data to ensure that the input shape is correct.In this case we must have the following shapes:

```ruby
  input_shape=(n_samples, know_points=20, vector_length=320)
  output_shape = vector_length
```
For this type of data we have trained 1D convolutional network whose structure can be seen in the following figure:
<p align="center">
  <img width="300" src="https://github.com/RoboticsURJC-students/2017-tfm-nuria-oyaga/blob/master/docs/Models/Non-Recurrent/Vector_URM/15_False_relu_categorical_crossentropy_10_properties.png">
</p>
As in the previous case, the network manages to reduce and stabilize the loss function in only a few epochs, without any error.
<p align="center">
  <img width="450" src="https://github.com/RoboticsURJC-students/2017-tfm-nuria-oyaga/blob/master/docs/Models/Non-Recurrent/Vector_URM/15_False_relu_categorical_crossentropy_10_history.png">
</p>
<p align="center">
  <img width="600" src="https://github.com/RoboticsURJC-students/2017-tfm-nuria-oyaga/blob/master/docs/Models/Non-Recurrent/Vector_URM/15_False_relu_categorical_crossentropy_10_error_hist.png">
</p>
In the next image you can see the samples where the errors (absolute and relative) are maximum. In this case we have not obtained any error so the first sample is shown.
<p align="center">
  <img width="600" src="https://github.com/RoboticsURJC-students/2017-tfm-nuria-oyaga/blob/master/docs/Models/Non-Recurrent/Vector_URM/15_False_relu_categorical_crossentropy_10_max_error.png">
</p>

### URM Point Frames dataset
As in the functions case, the first thing we must do to train the network for prediction is to resize the data to ensure that the input shape is correct.In this case we must have the following shapes:
```ruby
  input_shape=(n_samples, know_points=20, height=80, width=120)
  output_shape = height * width
```
For this type of data we have trained "D convolutional network whose structure can be seen in the following figure:
<p align="center">
  <img width="300" src="https://github.com/RoboticsURJC-students/2017-tfm-nuria-oyaga/blob/master/docs/Models/Non-Recurrent/Frame_point_URM/15_False_relu_categorical_crossentropy_10_properties.png">
</p>
As in the two previous cases, the network manages to reduce and stabilize the loss function in only a few epochs, without any error.
<p align="center">
  <img width="450" src="https://github.com/RoboticsURJC-students/2017-tfm-nuria-oyaga/blob/master/docs/Models/Non-Recurrent/Frame_point_URM/15_False_relu_categorical_crossentropy_10_history.png">
</p>
<p align="center">
  <img width="600" src="https://github.com/RoboticsURJC-students/2017-tfm-nuria-oyaga/blob/master/docs/Models/Non-Recurrent/Frame_point_URM/15_False_relu_categorical_crossentropy_10_error_hist.png">
</p>
In the next image you can see target frame in the samples where the errors (absolute and relative) are maximum. In this case we have not obtained any error so the first sample is shown.
<p align="center">
  <img width="800" src="https://github.com/RoboticsURJC-students/2017-tfm-nuria-oyaga/blob/master/docs/Models/Non-Recurrent/Frame_point_URM/15_False_relu_categorical_crossentropy_10_max_error.png">
</p>


## Data types
We will handle data of different nature that increase the degree of difficulty. The code to generate these samples can be found in https://github.com/RoboticsURJC-students/2017-tfm-nuria-oyaga/tree/master/Generator

### Linear Functions dataset
It is the simplest data to handle. The input of the network is a sequence of 20 numbers that follow the function of a line and the value that the network will return to us is the corresponding value of the function at point 20 + gap.

The samples are stored in a .txt file in which each line corresponds to a sample and the values of the function are stored in points [0,19] and 19 + gap.

In the following figure you can see an example of a sample of this type of functions:
<p align="center">
  <img width="460" src="https://github.com/RoboticsURJC-students/2017-tfm-nuria-oyaga/blob/master/docs/linear_function_sample.png">
</p>
To reduce complexity and avoid infinite slope lines, samples have been generated with a limitation in their slope defined in the configuration file.

### URM Vectors dataset
We increase the complexity of the previous data by increasing a dimension. We have created several 1D images in which the position of an object is represented at each moment of time. Each sample consists of 20 + 1 vectors, so that each vector consists of 320 positions and only activates (has a value of 255) that corresponds to the position in which the object would be found. To calculate the position we use a URM movement formula.

In the following figure you can see an example of a sample of this type of samples:
<p align="center">
  <img width="580" src="https://github.com/RoboticsURJC-students/2017-tfm-nuria-oyaga/blob/master/docs/vector_sample.png">
</p>
The 2D image represents in each row a continuous moment of time with the exception of the last row that corresponds to the position to be predicted with a gap of 10. In addition, the speed of the object is limited so that in the prediction the object is always in the image.

### URM Point Frames dataset
The next step to increase the complexity is to increase one more dimension. In this way, each sample will consist of 20 + 1 images (frames) in which the URM movement of an object will be represented through the time that is represented with a single pixel.

In the following video you can see an example of a sample of this type of samples:
<p align="center">
  <a href="http://www.youtube.com/watch?feature=player_embedded&v=RCEWNrTaYi8" target="_blank"><img src="https://github.com/RoboticsURJC-students/2017-tfm-nuria-oyaga/blob/master/docs/sample_0.png" 
  alt="journal analytics demo link to youtube" width="500"/></a>
</p>

As in the previous case, the speed of the object is limited so that in the prediction the object is always in the image.
