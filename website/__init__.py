from flask import Flask, render_template

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'minhahomerkey'

    from .views import views
    from .auth import aut