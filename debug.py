import peforth
peforth.ok(cmd='none value locals exit')
import tensorflow as tf
video = tf.keras.layers.Input(shape=(None,150,150,3))
cnn = tf.keras.applications.InceptionV3(
    weights='imagenet',
    include_top=False,
    pooling='avg')
cnn.trainable = False
encoded_frames = tf.keras.layers.TimeDistributed(cnn)(video)    
peforth.ok('Examine> ', loc=locals(),cmd=':> [0] to locals cr')
encoded_vid = tf.layers.LSTM(256)(encoded_frames)