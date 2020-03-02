from flask import Flask, request, render_template, flash
from utils.exif_extractor import get_exif_exiv2
import pyexiv2
import os
from contextlib import suppress

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/exifdata', methods=['POST', 'GET'])
def get_exif():
    exif_data = {}
    if request.method == 'POST':
        if request.files:
            image = request.files["exif-image"]
            imagepath = os.path.join(app.config['UPLOAD_FOLDER'],'tmp.jpg')
            image.save(imagepath)
            with suppress(AttributeError):
                exif_data = {key:values for key, values in get_exif_exiv2(imagepath)}
        if not exif_data:
            flash('{} has no EXIF data or is not a valid image file. '.format(image.filename))
        else:
            flash('Success.')
    return render_template('exifdata.html', exif_dict=exif_data)