import argparse
import os
import time
import tensorflow as tf
from tensorflow.python.client import device_lib

parser = argparse.ArgumentParser(description='TensorFlow benchmark')
parser.add_argument('--batch-size', type=int, default=256, metavar='N', help='batch size')
parser.add_argument('--epochs', type=int, default=10, metavar='N', help='number of epochs')
parser.add_argument('--data-dir', type=str, default='/tmp/mnist', metavar='PATH', help='path to data directory')
parser.add_argument('--log-dir', type=str, default='/tmp/tensorflow/logs', metavar='PATH', help='path to log directory')
parser.add_argument('--num-gpus', type=int, default=1, metavar='N', help='number of GPUs')
parser.add_argument('--gpu-ids', type=str, default='0', metavar='IDS', help='which GPUs to use')
parser.add_argument('--dtype', type=str, default='fp32', metavar='TYPE', help='data type (fp32|fp16)')
args = parser.parse_args()

os.environ['CUDA_VISIBLE_DEVICES'] = args.gpu_ids

def main():
    # Check the number of GPUs
    # num_gpus = validate_num_gpus(args.num_gpus)
    # Load the data
    train_data, test_data = load_data(args.data_dir, args.batch_size)
    # Create the model
    model = create_model(args.dtype, 0)
    # Train the model
    train(model, train_data, test_data, args.epochs)
    # Save the model
    save_model(model)

def validate_num_gpus(num_gpus):
    local_device_protos = device_lib.list_local_devices()
    num_available_gpus = len([x.name for x in local_device_protos if x.device_type == 'GPU'])
    if num_gpus < 1 or num_gpus > num_available_gpus:
        raise ValueError('num_gpus must be between 1 and %d' % num_available_gpus)
    return num_gpus

def load_data(data_dir, batch_size):
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    train_data = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(10000).batch(batch_size)
    test_data = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(batch_size)
    return train_data, test_data

def create_model(dtype, num_gpus):
    strategy = tf.distribute.MirroredStrategy(devices=['/gpu:%d' % i for i in range(num_gpus)])
    with strategy.scope():
        model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(512, activation='relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(10, activation='softmax')
        ])
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def train(model, train_data, test_data, epochs):
    log_dir = args.log_dir + '/' + time.strftime("%Y%m%d-%H%M%S")
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
    model.fit(train_data, epochs=epochs, validation_data=test_data, callbacks=[tensorboard_callback])

def save_model(model):
    model.save('mnist_model.h5')

if __name__ == '__main__':
    main()
