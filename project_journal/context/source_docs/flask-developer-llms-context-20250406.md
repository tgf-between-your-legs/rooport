TITLE: Creating Basic Flask Web Application in Python
DESCRIPTION: A simple Flask application example that creates a web server and returns 'Hello, World!' at the root route. This demonstrates the minimal setup required to create a Flask web application.

LANGUAGE: python
CODE:
# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

----------------------------------------

TITLE: Initializing Flask Application Factory in Python
DESCRIPTION: This code snippet demonstrates how to create an application factory function for a Flask app. It sets up configuration, creates necessary directories, and defines a simple route.

LANGUAGE: python
CODE:
import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

----------------------------------------

TITLE: Flask Extension Initialization Pattern
DESCRIPTION: Demonstrates the correct way to initialize Flask extensions using the factory pattern, showing both the incorrect direct initialization and the proper two-step initialization approach.

LANGUAGE: python
CODE:
def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    db = SQLAlchemy(app)

LANGUAGE: python
CODE:
db = SQLAlchemy()

LANGUAGE: python
CODE:
def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    from yourapplication.model import db
    db.init_app(app)

----------------------------------------

TITLE: Implementing User Registration View in Flask
DESCRIPTION: This snippet shows the implementation of a user registration view. It handles both GET and POST requests, validates user input, inserts new users into the database, and handles potential errors.

LANGUAGE: python
CODE:
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')

----------------------------------------

TITLE: Initializing SQLAlchemy with Declarative Mapping in Flask
DESCRIPTION: Sets up a basic SQLAlchemy configuration using the declarative approach with a SQLite database. Creates database session and base model class.

LANGUAGE: python
CODE:
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

engine = create_engine('sqlite:////tmp/test.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import yourapplication.models
    Base.metadata.create_all(bind=engine)

----------------------------------------

TITLE: Initializing a Flask Application in Python
DESCRIPTION: This snippet demonstrates how to create a basic Flask application, including configuration setup and defining a simple route. It shows the essential steps in the application setup phase.

LANGUAGE: python
CODE:
from flask import Flask

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY="dev",
)
app.config.from_prefixed_env()

@app.route("/")
def index():
    return "Hello, World!"

----------------------------------------

TITLE: Implementing Asynchronous Route Handler in Flask
DESCRIPTION: Demonstrates how to create an asynchronous route handler in Flask using async def and await. The example shows an async function querying a database and returning JSON data.

LANGUAGE: python
CODE:
@app.route("/get-data")
async def get_data():
    data = await async_db_query(...)
    return jsonify(data)

----------------------------------------

TITLE: Implementing File Upload and Validation in Flask
DESCRIPTION: Defines functions to check file extensions and handle file uploads. Includes a route for file upload with validation and secure saving of files.

LANGUAGE: python
CODE:
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

----------------------------------------

TITLE: Basic Flask Configuration Example
DESCRIPTION: Demonstrates basic configuration of a Flask application using dictionary-style access and the update method.

LANGUAGE: python
CODE:
app = Flask(__name__)
app.config['TESTING'] = True

app.config.update(
    TESTING=True,
    SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
)

----------------------------------------

TITLE: Configuring Flask for SPA and API
DESCRIPTION: This snippet shows how to set up a Flask application to serve a Single-Page Application and provide an API endpoint. It includes configuration for static file serving, a heartbeat endpoint for health checks, and a catch-all route for the SPA.

LANGUAGE: Python
CODE:
from flask import Flask, jsonify

app = Flask(__name__, static_folder='app', static_url_path="/app")


@app.route("/heartbeat")
def heartbeat():
    return jsonify({"status": "healthy"})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return app.send_static_file("index.html")

----------------------------------------

TITLE: Loading Flask Config from Python File
DESCRIPTION: Shows how to load Flask configuration from a Python module and environment variable.

LANGUAGE: python
CODE:
app = Flask(__name__)
app.config.from_object('yourapplication.default_settings')
app.config.from_envvar('YOURAPPLICATION_SETTINGS')

----------------------------------------

TITLE: Registering Flask Blueprint
DESCRIPTION: Shows how to register a blueprint with a Flask application, including examples of basic registration and registration with URL prefix.

LANGUAGE: python
CODE:
from flask import Flask
from yourapplication.simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)

----------------------------------------

TITLE: Initializing SQLite Database for Flask Application
DESCRIPTION: This snippet defines functions to initialize the database using the SQL schema and register a command-line command for database initialization. It also includes a converter registration for timestamp handling.

LANGUAGE: python
CODE:
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)

----------------------------------------

TITLE: Creating Basic Flask Blueprint
DESCRIPTION: Demonstrates how to create a simple Flask blueprint that renders static templates. The blueprint includes basic routing and template rendering with error handling.

LANGUAGE: python
CODE:
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        return render_template(f'pages/{page}.html')
    except TemplateNotFound:
        abort(404)

----------------------------------------

TITLE: Class-based Flask Configuration
DESCRIPTION: Example of using Python classes to manage different configuration environments like production, development and testing.

LANGUAGE: python
CODE:
class Config(object):
    TESTING = False

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DATABASE_URI = "sqlite:////tmp/foo.db"

class TestingConfig(Config):
    DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True

----------------------------------------

TITLE: Rendering a WTForms Form in a Jinja2 Template
DESCRIPTION: This HTML template demonstrates how to render a complete form using the previously defined macro. It iterates through the form fields and applies the render_field macro to each.

LANGUAGE: HTML
CODE:
{% from "_formhelpers.html" import render_field %}
<form method=post>
  <dl>
    {{ render_field(form.username) }}
    {{ render_field(form.email) }}
    {{ render_field(form.password) }}
    {{ render_field(form.confirm) }}
    {{ render_field(form.accept_tos) }}
  </dl>
  <p><input type=submit value=Register>
</form>

----------------------------------------

TITLE: Setting Content Security Policy Header in Flask
DESCRIPTION: Shows how to set a strict Content Security Policy (CSP) header in a Flask response to control resource loading.

LANGUAGE: python
CODE:
response.headers['Content-Security-Policy'] = "default-src 'self'"

----------------------------------------

TITLE: Defining a Registration Form Class with WTForms in Python
DESCRIPTION: This snippet demonstrates how to create a RegistrationForm class using WTForms. It includes various field types and validators for a typical user registration form.

LANGUAGE: Python
CODE:
from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

----------------------------------------

TITLE: Defining MongoDB Document Models with MongoEngine
DESCRIPTION: This snippet demonstrates how to define MongoDB document models using MongoEngine. It includes examples of basic field types and embedded documents.

LANGUAGE: python
CODE:
import mongoengine as me

class Movie(me.Document):
    title = me.StringField(required=True)
    year = me.IntField()
    rated = me.StringField()
    director = me.StringField()
    actors = me.ListField()

class Imdb(me.EmbeddedDocument):
    imdb_id = me.StringField()
    rating = me.DecimalField()
    votes = me.IntField()

class Movie(me.Document):
    ...
    imdb = me.EmbeddedDocumentField(Imdb)

----------------------------------------

TITLE: Configuring Flask Database Session Management
DESCRIPTION: Sets up automatic database session cleanup at the end of each request using Flask's teardown_appcontext decorator.

LANGUAGE: python
CODE:
from yourapplication.database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

----------------------------------------

TITLE: REST API Implementation using MethodView
DESCRIPTION: Complete REST API implementation using MethodView for handling different HTTP methods

LANGUAGE: python
CODE:
from flask.views import MethodView

class ItemAPI(MethodView):
    init_every_request = False

    def __init__(self, model):
        self.model = model
        self.validator = generate_validator(model)

    def _get_item(self, id):
        return self.model.query.get_or_404(id)

    def get(self, id):
        item = self._get_item(id)
        return jsonify(item.to_json())

    def patch(self, id):
        item = self._get_item(id)
        errors = self.validator.validate(item, request.json)

        if errors:
            return jsonify(errors), 400

        item.update_from_json(request.json)
        db.session.commit()
        return jsonify(item.to_json())

    def delete(self, id):
        item = self._get_item(id)
        db.session.delete(item)
        db.session.commit()
        return "", 204

----------------------------------------

TITLE: Handling JSON Responses in Flask Views
DESCRIPTION: Shows how to return JSON responses from Flask views using direct dict returns and jsonify.

LANGUAGE: python
CODE:
@app.route("/user/<int:id>")
def user_detail(id):
    user = User.query.get_or_404(id)
    return {
        "username": User.username,
        "email": User.email,
        "picture": url_for("static", filename=f"users/{id}/profile.png"),
    }

LANGUAGE: python
CODE:
from flask import jsonify

@app.route("/users")
def user_list():
    users = User.query.order_by(User.name).all()
    return jsonify([u.to_json() for u in users])

----------------------------------------

TITLE: Initializing and Managing SQLite3 Connection in Flask
DESCRIPTION: This snippet demonstrates how to set up a SQLite3 database connection in Flask, including connection initialization and automatic closing when the context ends. It uses Flask's app context and the 'g' object for efficient connection management.

LANGUAGE: Python
CODE:
import sqlite3
from flask import g

DATABASE = '/path/to/database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

----------------------------------------

TITLE: Blueprint Usage with Current App
DESCRIPTION: Shows how to access the application configuration within a blueprint using Flask's current_app context proxy. This approach allows blueprints to access application configuration without direct coupling.

LANGUAGE: python
CODE:
from flask import current_app, Blueprint, render_template
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
def index():
    return render_template(current_app.config['INDEX_TEMPLATE'])

----------------------------------------

TITLE: Applying Login Required Decorator to Flask Route
DESCRIPTION: This example demonstrates how to apply the login_required decorator to a Flask route, ensuring that only authenticated users can access the secret_page view.

LANGUAGE: python
CODE:
@app.route('/secret_page')
@login_required
def secret_page():
    pass

----------------------------------------

TITLE: Implementing Login Required Decorator in Python for Flask
DESCRIPTION: This code snippet defines a login_required decorator that checks if a user is logged in before allowing access to a view. It redirects to the login page if the user is not authenticated.

LANGUAGE: python
CODE:
from functools import wraps
from flask import g, request, redirect, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

----------------------------------------

TITLE: Initializing Blog Blueprint in Flask
DESCRIPTION: Sets up the basic blog blueprint with necessary imports and blueprint registration in the Flask application factory.

LANGUAGE: python
CODE:
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

LANGUAGE: python
CODE:
def create_app():
    app = ...
    # existing code omitted

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app

----------------------------------------

TITLE: Creating and Registering a Flask Blueprint for Authentication
DESCRIPTION: This snippet demonstrates how to create a Blueprint for authentication and register it with the Flask application. It sets up the basic structure for organizing authentication-related views.

LANGUAGE: python
CODE:
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

LANGUAGE: python
CODE:
def create_app():
    app = ...
    # existing code omitted

    from . import auth
    app.register_blueprint(auth.bp)

    return app

----------------------------------------

TITLE: Handling Form Submission and Validation in Flask View
DESCRIPTION: This code snippet shows how to handle form submission and validation in a Flask view function. It creates a form instance, validates the data, and processes it if valid.

LANGUAGE: Python
CODE:
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

----------------------------------------

TITLE: Initializing Flask Application Package
DESCRIPTION: Main __init__.py file that creates the Flask application instance and imports views. This is the core of the Flask package structure.

LANGUAGE: python
CODE:
from flask import Flask
app = Flask(__name__)

import yourapplication.views

----------------------------------------

TITLE: Creating a Convenient Query Function for SQLite3 in Flask
DESCRIPTION: This function simplifies database querying by combining cursor creation, query execution, and result fetching. It supports both multiple and single result queries, and includes proper cursor closure.

LANGUAGE: Python
CODE:
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

----------------------------------------

TITLE: Connecting to SQLite Database in Flask
DESCRIPTION: This snippet defines functions to connect to a SQLite database and close the connection. It uses Flask's g object for request-scoped data storage and current_app for accessing the application context.

LANGUAGE: python
CODE:
import sqlite3
from datetime import datetime

import click
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

----------------------------------------

TITLE: Configuring Basic Logging in Flask
DESCRIPTION: This code snippet shows how to configure basic logging for a Flask application using dictConfig. It sets up a formatter, a stream handler, and configures the root logger with an INFO level.

LANGUAGE: python
CODE:
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

----------------------------------------

TITLE: Basic Flask Message Flashing Implementation in Python
DESCRIPTION: Demonstrates a basic Flask application setup with message flashing functionality, including user login and flash message display. Uses Flask's flash() function to show success/error messages.

LANGUAGE: python
CODE:
from flask import Flask, flash, redirect, render_template, \
     request, url_for

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

----------------------------------------

TITLE: Generating Large CSV with Flask Route
DESCRIPTION: This snippet demonstrates how to create a Flask route that generates a large CSV file on the fly using a generator function.

LANGUAGE: python
CODE:
@app.route('/large.csv')
def generate_large_csv():
    def generate():
        for row in iter_all_rows():
            yield f"{','.join(row)}\n"
    return generate(), {"Content-Type": "text/csv"}

----------------------------------------

TITLE: Implementing a Generic Exception Handler for HTTP Errors
DESCRIPTION: Shows how to create a generic exception handler for HTTPException to return JSON instead of HTML for HTTP errors.

LANGUAGE: python
CODE:
from flask import json
from werkzeug.exceptions import HTTPException

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

----------------------------------------

TITLE: Logging User Login Attempts in Flask
DESCRIPTION: This snippet demonstrates how to log successful and failed login attempts using Flask's app.logger. It includes user authentication and redirects based on the login result.

LANGUAGE: python
CODE:
@app.route('/login', methods=['POST'])
def login():
    user = get_user(request.form['username'])

    if user.check_password(request.form['password']):
        login_user(user)
        app.logger.info('%s logged in successfully', user.username)
        return redirect(url_for('index'))
    else:
        app.logger.info('%s failed to log in', user.username)
        abort(401)

----------------------------------------

TITLE: Creating Base Layout Template in Flask with Jinja
DESCRIPTION: This snippet demonstrates how to create a base layout template using Jinja in Flask. It includes placeholders for title, header, and content, as well as conditional rendering for user authentication status.

LANGUAGE: html+jinja
CODE:
<!doctype html>
<title>{% block title %}{% endblock %} - Flaskr</title>
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<nav>
  <h1>Flaskr</h1>
  <ul>
    {% if g.user %}
      <li><span>{{ g.user['username'] }}</span>
      <li><a href="{{ url_for('auth.logout') }}">Log Out</a>
    {% else %}
      <li><a href="{{ url_for('auth.register') }}">Register</a>
      <li><a href="{{ url_for('auth.login') }}">Log In</a>
    {% endif %}
  </ul>
</nav>
<section class="content">
  <header>
    {% block header %}{% endblock %}
  </header>
  {% for message in get_flashed_messages() %}
    <div class="flash">{{ message }}</div>
  {% endfor %}
  {% block content %}{% endblock %}
</section>

----------------------------------------

TITLE: Storing Data in Flask g Object
DESCRIPTION: Demonstrates how to safely store extension-specific data in Flask's g object during a request. It shows two approaches: using a prefixed attribute name and using a namespace object.

LANGUAGE: python
CODE:
# an internal prefix with the extension name
g._hello_user_id = 2

# or an internal prefix as a namespace
from types import SimpleNamespace
g._hello = SimpleNamespace()
g._hello.user_id = 2

----------------------------------------

TITLE: Nginx Reverse Proxy Configuration
DESCRIPTION: Basic Nginx server configuration that sets up a reverse proxy to forward requests to a WSGI server running locally on port 8000. Includes necessary proxy headers for proper request forwarding.

LANGUAGE: nginx
CODE:
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:8000/;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Host $host;
        proxy_set_header X-Forwarded-Prefix /;
    }
}

----------------------------------------

TITLE: Configuring Flask Test Fixtures with Pytest
DESCRIPTION: Setup of basic pytest fixtures for Flask application testing, including app configuration, test client, and CLI runner setup.

LANGUAGE: python
CODE:
import pytest
from my_project import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()