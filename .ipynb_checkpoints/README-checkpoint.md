# Building High Performance Data Pipelines with tf.Data

In this article we present some recipes on how to build a data input pipeline using Tensorflow, specially tf.data.
It is recommended to read the first part, which defines the overall data and model, and then jump to any topic that interest you the most.

This article uses the Stanford Dogs Dataset with ~20000 images and 120 classes [1].


[1] Stanford Dataset - Dog Breeds

[] https://colab.sandbox.google.com/gist/robieta/9463e86b5501541a441d431b9c4f1a1e/tf_world.ipynb

## Step ONE

Read images one by one from a Google Cloud Storage bucket (gs).

Note that this may not be very efficient as we have a lot of small files to read (random reads).


## Step TWO

Consolidate images inside a TFRecord file. Use tf.examples protobuf to store all the bytes from images.

## Step THREE

Consolidate images already pre processed, using Apache Beam and TFRecord IO transform.

## Step FOUR

Use multiple GPUs to train our model.

## Step FIVE

Use Multiple workers to scale up the training.

### Other
 - Mixed Precision (optimize computation, but not IO)
 - Change Batch Size
 - Distributed Training (Strategy)
  - tf.distribute.MirroredStrategy
  - tf.distribute.MultiWorkerMirroredStrategy
  - tf.distribute.TPUStrategy
