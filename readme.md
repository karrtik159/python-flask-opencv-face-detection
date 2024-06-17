# Face Detection Web Application

This project is a web application that allows users to upload images or use their webcam to detect faces in real-time. The application uses OpenCV's Haar Cascade classifier to detect faces in images and display the results on the webpage.

## Features

- Upload an image file and detect faces.
- Capture an image from the webcam and detect faces.
- Display the number of detected faces and the processed image with rectangles drawn around the faces.

## Technologies Used

- Flask: A micro web framework for Python.
- OpenCV: An open-source computer vision library.
- HTML: For the web interface.
- JavaScript: For handling asynchronous requests (AJAX).

## Project Structure

```
├── app.py
├── templates
│   └── index.html
├── static
│   ├── frame.jpg
│   └── output.png
├── requirements.txt
└── README.md
```

- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML file for the web interface.
- `static/frame.jpg`: The temporary file to store the captured webcam image.
- `static/output.png`: The file to store the processed image with detected faces.
- `requirements.txt`: The file listing the Python dependencies.
- `README.md`: The file you are currently reading.

## Prerequisites

- Python 3.x
- Pip (Python package installer)
- OpenCV

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/tkmptech/python-flask-opencv-face-detection.git
   cd python-flask-opencv-face-detection
   ```

2. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the application:
   ```sh
   python app.py
   ```

4. Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

### Upload Image

1. On the home page, click the "Choose File" button to upload an image from your computer.
2. Click the "Upload" button to detect faces in the uploaded image.
3. The application will display the number of detected faces and the processed image with rectangles drawn around the faces.

### Capture Image from Webcam

1. On the home page, click the "Capture" button to take a picture using your webcam.
2. The application will detect faces in the captured image and display the number of detected faces and the processed image with rectangles drawn around the faces.

## Code Explanation

### `app.py`

- `index()`: Renders the home page.
- `upload()`: Handles the image upload, saves the file, and calls the `detect_faces` function.
- `analyse()`: Captures an image from the webcam, saves the frame, and calls the `detect_faces` function.
- `detect_faces(image_path)`: Detects faces in the given image using OpenCV's Haar Cascade classifier, draws rectangles around the faces, and saves the processed image.

### `templates/index.html`

The HTML file contains the structure of the web interface, including:

- A form to upload an image file.
- A button to capture an image from the webcam.
- A section to display the results (number of detected faces and processed image).

## Dependencies

- Flask
- OpenCV

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- OpenCV library for providing the tools to perform face detection.
- Flask framework for making web development easy and fun.

Feel free to contribute to this project by submitting issues or pull requests. Enjoy detecting faces!