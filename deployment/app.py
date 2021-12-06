from flask import Flask,render_template,Response
import cv2
import numpy as np
import os
import tensorflow as tf


app=Flask(__name__)
y_labels = ['Paper', 'Rock', 'Scissors']
model = tf.keras.models.load_model(os.path.join(app.root_path, 'static', 'model.h5'))

camera=cv2.VideoCapture(0)

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
        pred_label = y_labels[pred_binary[0]]
        pred_proba = '{:2.2f}%'.format(np.amax(pred_proba)*100)

        ai_label = y_labels[np.random.randint(0, len(y_labels))]
        ai_img = '{}.jpg'.format(ai_label)

        if (ai_label == 'Paper' and pred_label == 'Scissors') or (ai_label == 'Rock' and pred_label == 'Paper') or (ai_label == 'Scissors' and pred_label == 'Rock'):
            result_label = 'You win!'
        elif (pred_label == 'Paper' and ai_label == 'Scissors') or (pred_label == 'Rock' and ai_label == 'Paper') or (pred_label == 'Scissors' and ai_label == 'Rock'):
            result_label = 'You lose!'
        elif (pred_label == ai_label):
            result_label = 'Draw!'

        return render_template('prediction.html', 
                                probability = pred_proba, 
                                prediction = pred_label.upper(), 
                                display_image = 'input_imgs/' + frame_name,
                                game_choice = ai_label.upper(),
                                game_image = 'assets/img/choices/' + ai_img,
                                game_result = result_label.upper())

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)