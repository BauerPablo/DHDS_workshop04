import os
from flask import Flask, flash, request, redirect, url_for, render_template
from flask_dropzone import Dropzone
from werkzeug.utils import secure_filename

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
	'titulo': 'DELIVERY PREDICTOR',
	'area': 'Metrología'
	}

	return render_template('index.html', data=data)

@app.route('/como_funciona')
def como_funciona():

	data = {
	'titulo': '¿CÓMO FUNCIONA?',
	'area': 'Metrología'
	}

	return render_template('como_funciona.html', data=data)

def pagina_no_encontrada(error):

	data = {
	'titulo': 'Uuuupss... Creo que te equivocaste :-(',
	'area': 'Metrología'
	}

	return render_template('pagina_no_encontrada.html', data=data), 404

def allowed_file(filename):
	return'.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=['GET', 'POST'])
def upload_file():

	data = {
	'titulo': 'DELIVERY PREDICTOR',
	'area': 'Metrología'
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
			return render_template('index.html', data=data)

def calculator():
	pass



if  __name__ == '__main__':
	app.register_error_handler(404, pagina_no_encontrada)
	app.run(debug=True, port=5000)