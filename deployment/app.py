from flask import Flask,render_template,Response
import cv2
import numpy as np
import os
import tensorflow as tf


app=Flask(__name__)
camera=cv2.VideoCapture(0)
model = tf.keras.models.load_model(os.path.join(app.root_path, 'static', 'model.h5'))

y_labels = ['Paper', 'Rock', 'Scissors']

def generate_frames():
    while True:
        success,frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction', methods=['POST']) 
def pred():
    success,frame=camera.read()
    
    if success:
        frame 
        no = len(os.listdir(os.path.join(app.root_path, 'static', 'input_imgs')))
        frame_name = 'input_{}.jpg'.format(no)
        cv2.imwrite(os.path.join(app.root_path, 'static', 'input_imgs', frame_name), frame)  

        img = cv2.resize(frame, (224, 224)).reshape([1,224,224,3])
        pred_proba = model.predict(img)
        pred_binary = np.argmax(pred_proba, axis=1)

        return render_template('prediction.html' , probabilities = pred_proba, prediction = pred_binary, display_image = 'input_imgs/' + frame_name)

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)