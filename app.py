from flask import Flask, render_template, request, send_file, jsonify
import cv2
import numpy as np
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file_path = os.path.join('static', file.filename)
    file.save(file_path)
    output_path, num_faces = detect_faces(file_path)
    response = {
        'output_path' : output_path,
        'num_faces' : num_faces
    }
    return jsonify(response)

@app.route('/analyse', methods=['POST'])
def analyse():
    # file = request.files['file']
    camera = cv2.VideoCapture(0)
    success, frame = camera.read()  # read the camera frame
    frame = cv2.resize(frame, (224, 224))
    # r, jpg = cv2.imencode('.jpg', frame)
    file_path = os.path.join('static', 'frame.jpg')
    cv2.imwrite(file_path, frame)
    # file.save(file_path)
    
    output_path, num_faces = detect_faces(file_path)
    response = {
        'output_path' : output_path,
        'num_faces' : num_faces
    }
    return jsonify(response)



def detect_faces(image_path):
    #load the image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #load the pre-trained Haar Cascade classified for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0) , 5)

    # Save the result
    output_path = os.path.join('static', 'output.png')
    cv2.imwrite(output_path, img)

    return output_path, len(faces)

if __name__ == '__main__':
    app.run(debug=True)