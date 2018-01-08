import peforth
peforth.ok(cmd='none value locals exit')
import tensorflow as tf
video = tf.keras.layers.Input(shape=(None,150,150,3))
cnn = tf.keras.applications.InceptionV3(
    weights='imagenet',
    include_top=False,
    pooling='avg')
peforth.ok('Examine> ', loc=locals(),cmd=':> [0] to locals cr')
    