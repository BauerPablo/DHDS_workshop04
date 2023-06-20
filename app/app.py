
from flask import Flask, flash, request, redirect, url_for, render_template
from flask_dropzone import Dropzone
from werkzeug.utils import secure_filename
from sklearn.preprocessing import OneHotEncoder

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import pickle

UPLOAD_FOLDER = 'data/uploads'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config.update(
	UPLOAD_FOLDER = UPLOAD_FOLDER,
	DROPZONE_MAX_FILE_SIZE = 1024,
	DROPZONE_TIMEOUT = 5*60*1000
	)

dropzone = Dropzone(app)

@app.route('/')
def index():

	data = {
	'titulo': 'IRRADIANCE PREDICTOR',
	'area': 'Digital House - Data Science'
	}

	return render_template('index.html', data=data)

@app.route('/como_funciona')
def como_funciona():

	data = {
	'titulo': '¿CÓMO FUNCIONA?',
	'area': 'Digital House - Data Science'
	}

	return render_template('como_funciona.html', data=data)

def pagina_no_encontrada(error):

	data = {
	'titulo': 'Uuuupss... Creo que te equivocaste :-(',
	'area': 'Digital House - Data Science'
	}

	return render_template('pagina_no_encontrada.html', data=data), 404

def allowed_file(filename):
	return'.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=['GET', 'POST'])
def upload_file():

	data = {
	'titulo': 'IRRADIANCE PREDICTOR',
	'area': 'Digital House - Data Science'
	}

	if request.method == 'POST':
		
		file = request.files.get('file')
		print(app.config['UPLOAD_FOLDER'])

		if 'file' not in request.files:
			flash('Psss! falta el archivo. Amigow!')
			return render_template('index.html', data=data)

		if file.filename == '':
			flash('Psss! falta el archivo. Amigow!')
			return render_template('index.html', data=data)

		if file and allowed_file(file.filename):
			#filename = secure_filename(file.filename)
			file.save(os.path.join('data/uploads', file.filename))

			pred_dhi, pred_dni, pred_ghi = calculator(file)

			#Chequear si funciona asi. No estoy seguro si sirve
			data['prediccion_dhi'] = pred_dhi
			data['prediccion_dni'] = pred_dni
			data['prediccion_ghi'] = pred_ghi

			print(data)

			return render_template('index.html', data=data)

def calculator(file):

	model_file_name_dhi = 'predictors/dhi_model.pickle'
	model_file_name_dni = 'predictors/dni_model.pickle'
	model_file_name_ghi = 'predictors/ghi_model.pickle'

	model_dhi = pickle.load(open(model_file_name_dhi, 'rb'))
	model_dni = pickle.load(open(model_file_name_dni, 'rb'))
	model_ghi = pickle.load(open(model_file_name_ghi, 'rb'))

	data = pd.read_csv(os.path.join('data/uploads', file.filename), sep=',')
        
	data['cloud_type_cat'] = data['Cloud Type'].apply(cloud_type_cat)
	data['fill_flag_cat'] = data['Fill Flag'].apply(flag_cat)

	encoder = OneHotEncoder(drop='first', sparse=False)
	dummies = encoder.fit_transform(data[['cloud_type_cat', 'fill_flag_cat']])
	dummies = pd.DataFrame(dummies)
	dummies.columns = [x for cat_list in encoder.categories_ for x in cat_list[1:]]
	data = data.join(dummies)
	data = data.drop(columns=['Cloud Type','Fill Flag','cloud_type_cat','fill_flag_cat'])

	X = data.drop(['Clearsky DHI', 'Clearsky DNI','Clearsky GHI'], axis=1)

	print(data.shape)

	pred_dhi = model_dhi.predict(X)
	pred_dni = model_dni.predict(X)
	pred_ghi = model_ghi.predict(X)

	return pred_dhi, pred_dni, pred_ghi

def cloud_type_cat(x):
	    if x == 0:
	        return 'Clear'
	    elif x == 1:
	        return 'Probably_Clear'
	    elif x == 2:
	        return 'Fog'
	    elif x == 3:
	        return 'Water'
	    elif x == 4:
	        return 'Super_Cooled_Water'
	    elif x == 5:
	        return 'Mixed'
	    elif x == 6:
	        return 'Opaque_Ice'
	    elif x == 7:
	        return 'Cirrus'
	    elif x == 8:
	        return 'Overlapping'
	    elif x == 9:
	        return 'Overshooting'
	    elif x == 10:
	        return 'Unknown'
	    elif x == 11:
	        return 'Dust'
	    elif x == 12:
	        return 'Smoke'
	    elif x == -15:
	        return 'N/A'
	    else:
	        return np.nan

def flag_cat(x):
    if x == 0:
        return 'N/A'
    elif x == 1:
        return 'Missing_Image'
    elif x == 2:
        return 'Low_Irradiance'
    elif x == 3:
        return 'Exceeds_Clearsky'
    elif x == 4:
        return 'Missing_Cloud_Properties'
    elif x == 5:
        return 'Rayleigh_Violation'
    else:
        return 'Other'

if  __name__ == '__main__':
	app.register_error_handler(404, pagina_no_encontrada)
	app.run(debug=True, port=5000)