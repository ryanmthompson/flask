__author__ = 'rthompson'

import flask
import flask_login
import configuration_service
import database_service
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.triangle import Triangle
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from flask_socketio import SocketIO, send, emit

app = flask.Flask(__name__)

configuration_service.configure(app)

login_manager = flask_login.LoginManager()

login_manager.init_app(app)

# Our mock database.
users = {'foo@bar.tld': {'pw': 'secret'}}

db = SQLAlchemy(app)
database_service.initialize_relationships(db)
database_service.build_sample_db(db)


# Instantiate AngularJS parsing
# e.g. {{expression|angular}}
Triangle(app)

# Instantiate web sockets
socketio = SocketIO(app)


# Define database relationships
# Create User/Role relationship
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('roles.id')))

# Create Site/Assessment relationship
assessments_sites = db.Table('assessments_sites',
                             db.Column('site_id', db.Integer(), db.ForeignKey('sites.id')),
                             db.Column('assessment_id', db.Integer(), db.ForeignKey('assessments.id')))


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['pw'] == users[email]['pw']

    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'></input>
                <input type='password' name='pw' id='pw' placeholder='password'></input>
                <input type='submit' name='submit'></input>
               </form>
               '''

    email = flask.request.form['email']
    if flask.request.form['pw'] == users[email]['pw']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))

    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'

app.run(host='0.0.0.0', port='5050')