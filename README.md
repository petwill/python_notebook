# python notebook

* force keras to use cpu

`
import os<br>
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"<br>
os.environ["CUDA_VISIBLE_DEVICES"] = ""<br>
`

* set tensorflow gpu usage

`
import tensorflow as tf<br>
from keras.backend.tensorflow_backend import set_session<br>
config = tf.ConfigProto()<br>
config.gpu_options.per_process_gpu_memory_fraction = 0.3<br>
set_session(tf.Session(config=config))<br>
`
