import tensorflow_datasets as tfds
import tensorflow as tf
import os

BUFFER_SIZE = 10000
BATCH_SIZE = 32

def model_fn(learning_rate):
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, 3, activation='relu', input_shape=(28, 28, 1)),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10)
    ])

    return compile_model_fn(model, learning_rate)

def compile_model_fn(model, learning_rate):
    model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                metrics=['accuracy'])

    return model

def scale(image, label):
    image = tf.cast(image, tf.float32)
    image /= 255

    return image, label

def get_dataset(batch_size=BATCH_SIZE, buffer_size=BUFFER_SIZE):
    datasets, info = tfds.load(name='mnist', with_info=True, as_supervised=True)
    mnist_train, mnist_test = datasets['train'], datasets['test']

    train_dataset = mnist_train.map(scale).cache().shuffle(buffer_size).batch(batch_size)
    eval_dataset = mnist_test.map(scale).batch(batch_size)

    return train_dataset, eval_dataset