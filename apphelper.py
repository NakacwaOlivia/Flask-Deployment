import tensorflow as tf
import numpy as np

def get_class(file_path):
    model = tf.keras.models.load_model('model.h5')

    test =tf.keras.preprocessing.image.load_img(file_path, target_size=(64, 64))  
    test = tf.keras.preprocessing.image.img_to_array(test)
    test = np.expand_dims(test, axis=0)
    result = model.predict(test)
    if result[0][0] == 1:
        prediction = 'healthy'
    else:
        prediction = 'affected (fall army worm)'
    return prediction, result[0][0]

