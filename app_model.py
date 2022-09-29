from flask import Flask, flash,  request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

import os
import pickle
import pandas as pd
import numpy as np
import pygit as git

os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv','txt','xls'}

# In a real app, the secret key would be in a separate config file and not visible in the source control
app.config['SECRET_KEY'] = '\xf7\xc4\xd3:\xdfH\x84h\xcd\xa9\xa5t\xbe\x13\x18L\x0e&\xf8\xc8}\xf9\xe9s'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Route for the GitHub webhook

@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./TBDS_ML_Clf_WaterQuality_flask')
    origin = repo.remotes.origin
    repo.create_head('main',
                     origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200


@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/predict", methods=['POST'])
def predict():
    
    if 'chooseFile' not in request.files:
        flash('No file part')
        return redirect(url_for(home))
    file = request.files['chooseFile']

    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for(home))

    if file and allowed_file(file.filename):
        datos = pd.read_csv(file)
        tamano = len(datos)
        scaler = pickle.load(open('scaler.pkl', 'rb'))
        model = pickle.load(open('model_selected.pkl', 'rb'))
        datos_scaled = scaler.transform(datos)
        prediction = model.predict(datos_scaled)
        
        if tamano>1:
            tabla = pd.DataFrame(datos,columns=datos.columns)
            resultado = ['safe' if p==1 else 'not safe' for p in prediction ]
            tabla.insert(0,'prediction',resultado)
            return render_template('predict_table.html',  tables=[tabla.to_html(classes='data', header="true")])
            
        elif tamano==1:
            return render_template('predict.html',resultado=prediction[0])
            