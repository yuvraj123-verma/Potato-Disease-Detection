# # from flask import Flask, render_template, Response
# #
# # app = Flask(__name__)
# #
# # @app.route('/')
# # def home():
# #     return render_template('index.html')
# #
# #
# # if __name__ == '__main__':
# #     app.run(debug=True)
#
# import tensorflow as tf
# import numpy as np
# from tensorflow.keras import models
# import cv2
# model = tf.keras.models.load_model('test.h5')
#
# CLASS_NAMES = ['Tomato_Early_blight', 'Tomato_Late_blight', 'Tomato_healthy']
#
# def predict(model, img):
#     img_array = tf.keras.preprocessing.image.img_to_array(img)
#     img_array = tf.expand_dims(img_array, 0)
#
#     predictions = model.predict(img_array)
#
#     predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
#     confidence = round(100 * (np.max(predictions[0])), 2)
#
#     return predicted_class, confidence
#
# image = cv2.imread(r'F:\Potato disease detection\PlantVillage\Potato___Early_blight\0a8a68ee-f587-4dea-beec-79d02e7d3fa4___RS_Early.B 8461.JPG')
# class_, lab  = predict(model, image)
# print(class_, lab)
import tensorflow as tf
print(tf.__version__)