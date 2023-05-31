from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

	data = {
	'titulo': 'PREDICTOR DE IRRADIACIÓN',
	'area': 'Workshop 4 - Grupo 8'
	}

	return render_template('index.html', data=data)

@app.route('/como_funciona')
def como_funciona():

	data = {
	'titulo': '¿CÓMO FUNCIONA?',
	'area': 'Workshop 4 - Grupo 8'
	}

	return render_template('como_funciona.html', data=data)

@app.route('/sobre_el_workshop_04')
def sobre_el_workshop_04():

	data = {
	'titulo': 'SOBRE EL WORKSHOP',
	'area': 'Workshop 4 - Grupo 8'
	}

	return render_template('sobre_el_workshop_04.html', data=data)

@app.route('/grupo_8')
def grupo_8():

	data = {
	'titulo': 'GRUPO 8',
	'area': 'Workshop 4 - Grupo 8'
	}

	return render_template('grupo_8.html', data=data)

def pagina_no_encontrada(error):

	data = {
	'titulo': 'Uuuupss... Creo que te equivocaste :-(',
	'area': 'Workshop 4 - Grupo 8'
	}

	return render_template('pagina_no_encontrada.html', data=data), 404

if  __name__ == '__main__':
	app.register_error_handler(404, pagina_no_encontrada)
	app.run(debug=True, port=5000)