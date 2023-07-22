# from flask import Flask, request, render_template
# from keras_preprocessing import image
# from keras.models import load_model
# from keras.applications.vgg16 import preprocess_input
# import numpy as np
# import os

# model = load_model('our_model.h5')

# def predict_pneumonia(file):
#     img = image.load_img(file, target_size=(224, 224))
#     x = image.img_to_array(img)
#     x = np.expand_dims(x, axis=0)
#     x = preprocess_input(x)
#     prediction = model.predict(x)
#     return prediction[0][0] > prediction[0][1]

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     file = request.files['image']
#     filename = file.filename
#     file_path = os.path.join('static', filename)
#     file.save(file_path)
#     result = predict_pneumonia(file_path)
#     if result:
#         prediction = 'Person is affected with Pneumonia.'
#     else:
#         prediction = 'Person is safe.'
#     return render_template('predict.html', prediction=prediction, image_path=file_path)

# if __name__ == "__main__":
#     app.run(debug=True, port= 5000)


from flask import Flask, request, render_template
from keras_preprocessing import image
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
import numpy as np
import os
import cv2

model = load_model('trained.h5')

def predict_pneumonia(file):
    img= cv2.imread(file)
    tempimg = img
    img = cv2.resize(img,(300,300))
    img = img/255.0
    img = img.reshape(1,300,300,3)
    model.predict(img)
    prediction = model.predict(img)
    return prediction >= 0.5

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files['image']
        filename = file.filename
        file_path = os.path.join('static/database', filename)
        file.save(file_path)
        result =predict_pneumonia(file_path)
        if result:
            prediction = "Pneumonia"
        else:
            prediction = "Normal"
        return render_template('predict.html', prediction=prediction, image_path=file_path)
    except:
        prediction="File not found"
        return render_template('predict.html', prediction=prediction)
if __name__ == "__main__":
    app.run(debug=True, port= 5000)
    