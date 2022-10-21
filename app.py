from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from apphelper import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/predict", methods = ['POST'])
def upload_file():

    if request.method == 'POST':
        f = request.files['file']

        try:
            # Save the file to ./uploads folder
            basepath = os.path.dirname(__file__)
            print(basepath)
            file_path = os.path.join(basepath, 'static','uploads', secure_filename(f.filename))
            f.save(file_path)

            # get prediction from the apphelper.py by calling the "get_class" function
            prediction=get_class(file_path)
            score=prediction[1]
            prediction=prediction[0]
            
        except FileNotFoundError:
            return render_template("base.html")
        
    return render_template("upload.html", predictions=prediction, display_image=f.filename, scores=score)


if __name__ == '__main__':
    #app.debug = True
    app.run(debug=True,use_reloader=False)
