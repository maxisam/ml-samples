import argparse
import glob
import os

import trainer.model as model

def train_model(args):
    mnist_model = model.model_fn(args.learning_rate)
    train_dataset, eval_dataset = model.get_dataset(args.train_batch_size)

    history = mnist_model.fit(train_dataset, epochs=args.num_epochs)

    eval_loss, eval_acc = mnist_model.evaluate(eval_dataset)
    print('Eval loss: {}, Eval Accuracy: {}'.format(eval_loss, eval_acc))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--train-batch-size',
        type=int,
        default=32,
        help='Batch size for training steps')
    parser.add_argument(
        '--learning-rate',
        type=float,
        default=0.001,
        help='Learning rate for SGD')
    parser.add_argument(
        '--num-epochs',
        type=int,
        default=10,
        help='Maximum number of epochs on which to train')

    args, _ = parser.parse_known_args()
    train_model(args)