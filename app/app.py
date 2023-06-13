import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/data/uploads'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

@app.route("/", methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		if 'file' not in request.files:
			flash('Psss! no es el archivo')
			return redirect(request.url)

		file = request.files['file']

		if file.filename == '':
			flash('Psss! falta el archivo. Amigow!')
			return redirect(request.url)

		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('downlad_file', name=filename))

def calculator():
	pass



if  __name__ == '__main__':
	app.register_error_handler(404, pagina_no_encontrada)
	app.run(debug=True, port=5000)