import keras
    from keras.applications.vgg16 import VGG16
    from keras.preprocessing import image
    from keras.engine import Layer
    from keras.applications.inception_resnet_v2 import preprocess_input
    from keras.layers import Conv2D UpSampling2D InputLayer Conv2DTranspose Input Reshape merge concatenate
    from keras.layers import Activation Dense Dropout Flatten
    from keras.layers.normalization import BatchNormalization
    from keras.callbacks import TensorBoard 
    from keras.models import Sequential Model
    from keras.layers.core import RepeatVector Permute
    from keras.preprocessing.image import ImageDataGenerator array_to_img img_to_array load_img
    from skimage.color import rgb2lab lab2rgb rgb2gray gray2rgbrgb2luvluv2rgbrgb2graygray2rgb
    from skimage.transform import resize
    from skimage.io import imsave
    import numpy as np
    import os
    import random
    import tensorflow as tf