from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

def create_dash_app(flask_app):
	dash_app = Dash(server=flask_app, name='Dashboard', url_base_pathname="/dash/")

	dash_app.layout = html.Div([
	    html.H1('Hello Dash')
	])

	return dash_app.layout