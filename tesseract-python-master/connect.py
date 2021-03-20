# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import webbrowser
# import our OCR function
from image_example import ocr_core

# define a folder to store and later serve the images
UPLOAD_FOLDER = '/'

# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__, template_folder='C:/Users/Dell/Anaconda3/tesseract-python-master')


# function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('index.html', msg='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('index.html', msg='No file selected')

        if file and allowed_file(file.filename):
            extracted_text = ocr_core(file)
            return render_template('index.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text,
                                   img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000/', new=2)
    app.run()
    